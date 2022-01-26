from blog import db
from blog.models import User, Post, Comment, Rating

def add_post(post):
    db.session.add(post)
    db.session.commit()


title = "This is the fourth post"
content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
summary ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tincidunt id aliquet risus feugiat in ante metus dictum at. Vitae suscipit tellus mauris a diam maecenas sed enim."
image_file ="default.jpg" 
author_id = 2
post = Post(title = title, content = content, summary = summary, image_file = image_file, author_id = author_id)
add_post(post)


