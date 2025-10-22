#!/bin/bash
#
# mail_to_api.sh
# Forwards selected emails as JSON to API endpoint
#

API_URL= "api.domain.com/endpoint" # Replace with your API endpoint

# Read full email from stdin into a variable
EMAIL=$(cat)

# Extract headers
FROM=$(echo "$EMAIL" | grep -m1 "^From:" | cut -d' ' -f2-)
TO=$(echo "$EMAIL" | grep -m1 "^To:" | cut -d' ' -f2-)
SUBJECT=$(echo "$EMAIL" | grep -m1 "^Subject:" | cut -d' ' -f2-)

# Extract body (everything after first blank line)
BODY=$(echo "$EMAIL" | sed -n '/^$/,$p' | tail -n +2)

# Build JSON payload with new key names
JSON=$(jq -n \
  --arg from "$FROM" \
  --arg to "$TO" \
  --arg subject "$SUBJECT" \
  --arg body "$BODY" \
  '{from:$from, to:$to, subject:$subject, body:$body}')
+
# Send to API
curl -s -X POST "$API_URL" \
  -H "Content-Type: application/json" \
  -d "$JSON"

exit 0
