
# Django Permissions and Groups Management

## Objective
Implement and manage permissions and groups to control access to various parts of your Django application, enhancing security and functionality.

## Task Description
Develop a system within your Django application that utilizes groups and permissions to restrict access to certain parts of the application. This task demonstrates the ability to set up detailed access controls based on user roles and their assigned permissions.

## Steps to Implement

### Step 1: Define Custom Permissions in Models
- **Model**: The permissions have been added to the `Book` model (or your chosen model) to control actions such as viewing, creating, editing, or deleting instances of that model.
  
  **Custom Permissions**:
  - `can_view`: Permission to view books.
  - `can_create`: Permission to create new book entries.
  - `can_edit`: Permission to edit existing book entries.
  - `can_delete`: Permission to delete book entries.

### Step 2: Create and Configure Groups with Assigned Permissions
- **Groups Created**:
  - **Editors**: Assigned `can_edit` and `can_create` permissions.
  - **Viewers**: Assigned `can_view` permission.
  - **Admins**: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

- **Group Management**: Groups and their permissions can be managed via the Django admin site.

### Step 3: Enforce Permissions in Views
- **Views Modified**: Relevant views have been updated to include permission checks using decorators.
  
  **Example**:
  ```python
  @permission_required('bookshelf.can_edit', raise_exception=True)
  def edit_book(request, book_id):
      ...