# Management API app - continuation

## Part 2: Permissions:

### Enabling Permissions:

- To regulate access to our API views, you'll be integrating custom permissions.
  
- Start by crafting a `IsDepartmentAdmin` permission class in the `permissions.py` file. Inherit attributes from `rest_framework.permissions.BasePermission` and implement the `has_object_permission` function. This function should ascertain if the requesting user is a department administrator, returning `True` if affirmative, or `False` otherwise.

- In all the view classes (`DepartmentListView`, `DepartmentCreateView`, `EmployeeListView`, `EmployeeCreateView`, `TaskRetrieveView`, and `TaskUpdateView`), integrate the `permission_classes` attribute, setting its value to `[permissions.IsDepartmentAdmin]` to enforce the bespoke permission.

- To ascertain permission functionality, test the API with two scenarios: a non-administrator user and a department administrator.

## Part 3: Hyperlinks (BONUS):

### Enhancing Navigation:

- To elevate our API's navigation, we'll be infusing hyperlinks into our API responses.
  
- For every model (Department, Employee, and Task), design a serializer class inheriting from `serializers.HyperlinkedModelSerializer` as opposed to the `serializers.ModelSerializer`.
  
- Within each of these serializer classes, introduce the `url` field, associating it with `serializers.HyperlinkedIdentityField(view_name='{model_name}-detail')` where `{model_name}` symbolizes the lowercase model name (e.g., `department`, `employee`, `task`).

- Upgrade the view classes (`DepartmentListView`, `DepartmentCreateView`, `EmployeeListView`, `EmployeeCreateView`, `TaskRetrieveView`, and `TaskUpdateView`) to incorporate these new serializer classes.

- Ensure your API now showcases responses inclusive of hyperlinks directing to the details of each object.