
const { test } = require('tap')
const build = require('./index')

test('Run test on generate password route: ', async t => {
  const response = await build.inject({
    method: 'GET',
    url: '/'
  })
  t.equal(response.statusCode, 200, 'returns a status code of 200');
  t.equal(JSON.parse(response.body).success, true, "returned success true");
})