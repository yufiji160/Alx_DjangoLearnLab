# Django Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model (`models.py`):
- can_view
- can_create
- can_edit
- can_delete

## Groups
Created in `setup_groups.py`:
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: can_view, can_create, can_edit, can_delete

## Permission Enforcement
In `views.py`, views are protected using `@permission_required()` decorators:
- list_books → `relationship_app.can_view`
- add_book → `relationship_app.can_create`
- edit_book → `relationship_app.can_edit`
- delete_book → `relationship_app.can_delete`

Run the setup in shell:
```bash
python3 manage.py shell
>>> from relationship_app.setup_groups import setup_groups_and_permissions
>>> setup_groups_and_permissions()
