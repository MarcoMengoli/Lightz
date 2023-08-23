import express from "express";

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/x", (req, res) => {
  throw new Error("This is an example exception.");
});

app.listen(PORT, () => {
  console.log("Server listening on port ${PORT}");
});
