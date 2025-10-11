# Tagging & Search — User Guide


## Adding tags to a post
- When creating or editing a post, the Tags field accepts comma-separated tags (e.g. `django, tips`).
- Save the post — tags are created automatically.


## Finding posts
- Use the search box in the header to search by keyword or tag.
- Click a tag underneath any post to see all posts with that tag.


## Admin / dev notes
- This feature uses `django-taggit`.
- To add/remove tags programmatically: `post.tags.add('tag')`, `post.tags.remove('tag')`, or `post.tags.set(['a', 'b'])`.