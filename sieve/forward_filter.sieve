require ["fileinto", "copy"];

if allof( #make changes to the if condition as per your requirement
  address :is "From" "email-address", #enter sender email address
  header :contains "Subject" "Email-Subject" #enter Subject of email to be filtered
) {
  redirect "forward-to-email-address"; #enter destination email address
}
