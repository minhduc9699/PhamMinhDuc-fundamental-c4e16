from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db['posts']

new_post = {
    "title" : "Tuyên ngôn... học code",
    "author" : "Minh Đức",
    "content" : """Hỡi đồng bào cả nước,
    tất cả mọi người sinh ra đều có quyền bình đẳng. Tạo hóa cho họ những quyền không ai có thể xâm phạm được;
    trong những quyền ấy, có quyền được học code, quyền tự do viết code, và quyền compile code."""
}

posts.insert_one(new_post)
