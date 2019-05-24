
conn = new Mongo();

db = conn.getDB('admin');

db.auth('root', 'example');

db = db.getSiblingDB('pixeldb');

db.createUser({
    user: 'user',
    pwd: 'password',
    roles: [{ role: 'readWrite', db: 'pixeldb' }],
});