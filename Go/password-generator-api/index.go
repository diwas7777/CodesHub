package main

import (
    "log"
    "github.com/gofiber/fiber/v2"
	"github.com/matoous/go-nanoid/v2"
)

func main() {
    app := fiber.New()

    app.Get("/", func (c *fiber.Ctx) error {
		id, err := gonanoid.Generate("abcdefg", 10)
		if err != nil {
			panic(err)
		}
        return c.SendString(id)
    })

    log.Fatal(app.Listen(":3000"))
}