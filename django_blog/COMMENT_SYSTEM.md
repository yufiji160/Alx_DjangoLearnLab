# Django Blog Comment System

## Features
- Users can add, edit, and delete comments on posts.
- Only the author of a comment can modify or delete it.
- Comments are displayed under each post.

## How It Works
- **Model:** `Comment` links `User` and `Post`.
- **Forms:** `CommentForm` for create/update.
- **Views:** Handles add, edit, and delete operations.
- **Templates:** Integrated in `post_detail.html`.

## URL Patterns
- `/post/<int:pk>/comments/new/` → Add new comment.
- `/comment/<int:pk>/update/` → Edit comment.
- `/comment/<int:pk>/delete/` → Delete comment.

## Permissions
- Only logged-in users can comment.
- Only comment authors can edit or delete their comments.
# Django Blog Comment System
