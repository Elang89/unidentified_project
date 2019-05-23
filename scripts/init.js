conn = new Mongo();
db = conn.getDB("admin");
db.auth("admin", "password");

db = db.getSiblingDB("plpdb");
db.auth("user", "password");

db.createUser(
    {
        user: "user",
        pwd: "password",
        roles: [ {role: "readWrite", db: "plpdb"}]
    }
);

