## Blog Post Management

This feature enables authenticated users to create, edit, and delete their blog posts, while all users can read posts.

### Features
- **ListView**: `/posts/` — View all posts.
- **DetailView**: `/posts/<id>/` — View a single post.
- **CreateView**: `/posts/new/` — Authenticated users can create posts.
- **UpdateView**: `/posts/<id>/edit/` — Only the post author can edit.
- **DeleteView**: `/posts/<id>/delete/` — Only the post author can delete.

### Permissions
- Unauthenticated users: Can only view posts.
- Authenticated users: Can create posts.
- Authors: Can edit or delete their own posts.
