var mysql = require("mysql2");
var db = mysql.createConnection({
  host: "127.0.0.1",
  user: "dogyun",
  password: "1234",
  database: "mail",
  dateStrings: "date",
});
module.exports = db;