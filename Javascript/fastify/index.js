const fastify = require("fastify")({ logger: true });
const { customAlphabet } = require("nanoid");
const alphabets =
  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
const nanoid = customAlphabet(alphabets, 16);

fastify.route({
  method: "GET",
  url: "/",
  schema: {
    querystring: {
      size: { type: ["string", "null"], nullable: true,},
    },
    response: {
      200: {
        type: "object",
        properties: {
          password: { type: "string" },
          success: { type: "boolean" },
          createdAt: { type: "number" },
        },
      },
    },
  },
  handler: async (request, reply) => {
    return {
      password: nanoid(request.size),
      createdAt: +new Date(),
      success: true,
    };
  },
});

const start = async () => {
  try {
    await fastify.listen({ port: 3000 });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};
start();
