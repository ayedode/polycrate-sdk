from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notes_list_assigned_to_error_component import ApiV1NotesListAssignedToErrorComponent
    from ..models.api_v1_notes_list_created_by_users_error_component import ApiV1NotesListCreatedByUsersErrorComponent
    from ..models.api_v1_notes_list_datasource_error_component import ApiV1NotesListDatasourceErrorComponent
    from ..models.api_v1_notes_list_has_time_tracked_error_component import ApiV1NotesListHasTimeTrackedErrorComponent
    from ..models.api_v1_notes_list_kind_error_component import ApiV1NotesListKindErrorComponent
    from ..models.api_v1_notes_list_managed_by_object_id_error_component import (
        ApiV1NotesListManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_notes_list_name_exact_error_component import ApiV1NotesListNameExactErrorComponent
    from ..models.api_v1_notes_list_organizations_error_component import ApiV1NotesListOrganizationsErrorComponent
    from ..models.api_v1_notes_list_parent_note_error_component import ApiV1NotesListParentNoteErrorComponent
    from ..models.api_v1_notes_list_project_error_component import ApiV1NotesListProjectErrorComponent
    from ..models.api_v1_notes_list_search_error_component import ApiV1NotesListSearchErrorComponent
    from ..models.api_v1_notes_list_state_error_component import ApiV1NotesListStateErrorComponent
    from ..models.api_v1_notes_list_state_not_error_component import ApiV1NotesListStateNotErrorComponent
    from ..models.api_v1_notes_list_time_range_error_component import ApiV1NotesListTimeRangeErrorComponent
    from ..models.api_v1_notes_list_time_tracked_min_error_component import ApiV1NotesListTimeTrackedMinErrorComponent
    from ..models.api_v1_notes_list_workspaces_error_component import ApiV1NotesListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1NotesListValidationError")


@_attrs_define
class ApiV1NotesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotesListAssignedToErrorComponent | ApiV1NotesListCreatedByUsersErrorComponent |
            ApiV1NotesListDatasourceErrorComponent | ApiV1NotesListHasTimeTrackedErrorComponent |
            ApiV1NotesListKindErrorComponent | ApiV1NotesListManagedByObjectIdErrorComponent |
            ApiV1NotesListNameExactErrorComponent | ApiV1NotesListOrganizationsErrorComponent |
            ApiV1NotesListParentNoteErrorComponent | ApiV1NotesListProjectErrorComponent |
            ApiV1NotesListSearchErrorComponent | ApiV1NotesListStateErrorComponent | ApiV1NotesListStateNotErrorComponent |
            ApiV1NotesListTimeRangeErrorComponent | ApiV1NotesListTimeTrackedMinErrorComponent |
            ApiV1NotesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotesListAssignedToErrorComponent
        | ApiV1NotesListCreatedByUsersErrorComponent
        | ApiV1NotesListDatasourceErrorComponent
        | ApiV1NotesListHasTimeTrackedErrorComponent
        | ApiV1NotesListKindErrorComponent
        | ApiV1NotesListManagedByObjectIdErrorComponent
        | ApiV1NotesListNameExactErrorComponent
        | ApiV1NotesListOrganizationsErrorComponent
        | ApiV1NotesListParentNoteErrorComponent
        | ApiV1NotesListProjectErrorComponent
        | ApiV1NotesListSearchErrorComponent
        | ApiV1NotesListStateErrorComponent
        | ApiV1NotesListStateNotErrorComponent
        | ApiV1NotesListTimeRangeErrorComponent
        | ApiV1NotesListTimeTrackedMinErrorComponent
        | ApiV1NotesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notes_list_assigned_to_error_component import ApiV1NotesListAssignedToErrorComponent
        from ..models.api_v1_notes_list_created_by_users_error_component import (
            ApiV1NotesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_notes_list_datasource_error_component import ApiV1NotesListDatasourceErrorComponent
        from ..models.api_v1_notes_list_has_time_tracked_error_component import (
            ApiV1NotesListHasTimeTrackedErrorComponent,
        )
        from ..models.api_v1_notes_list_kind_error_component import ApiV1NotesListKindErrorComponent
        from ..models.api_v1_notes_list_managed_by_object_id_error_component import (
            ApiV1NotesListManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_notes_list_organizations_error_component import ApiV1NotesListOrganizationsErrorComponent
        from ..models.api_v1_notes_list_parent_note_error_component import ApiV1NotesListParentNoteErrorComponent
        from ..models.api_v1_notes_list_project_error_component import ApiV1NotesListProjectErrorComponent
        from ..models.api_v1_notes_list_search_error_component import ApiV1NotesListSearchErrorComponent
        from ..models.api_v1_notes_list_state_error_component import ApiV1NotesListStateErrorComponent
        from ..models.api_v1_notes_list_state_not_error_component import ApiV1NotesListStateNotErrorComponent
        from ..models.api_v1_notes_list_time_range_error_component import ApiV1NotesListTimeRangeErrorComponent
        from ..models.api_v1_notes_list_time_tracked_min_error_component import (
            ApiV1NotesListTimeTrackedMinErrorComponent,
        )
        from ..models.api_v1_notes_list_workspaces_error_component import ApiV1NotesListWorkspacesErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListAssignedToErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListDatasourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListParentNoteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListProjectErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListHasTimeTrackedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListTimeTrackedMinErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_notes_list_assigned_to_error_component import ApiV1NotesListAssignedToErrorComponent
        from ..models.api_v1_notes_list_created_by_users_error_component import (
            ApiV1NotesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_notes_list_datasource_error_component import ApiV1NotesListDatasourceErrorComponent
        from ..models.api_v1_notes_list_has_time_tracked_error_component import (
            ApiV1NotesListHasTimeTrackedErrorComponent,
        )
        from ..models.api_v1_notes_list_kind_error_component import ApiV1NotesListKindErrorComponent
        from ..models.api_v1_notes_list_managed_by_object_id_error_component import (
            ApiV1NotesListManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_notes_list_name_exact_error_component import ApiV1NotesListNameExactErrorComponent
        from ..models.api_v1_notes_list_organizations_error_component import ApiV1NotesListOrganizationsErrorComponent
        from ..models.api_v1_notes_list_parent_note_error_component import ApiV1NotesListParentNoteErrorComponent
        from ..models.api_v1_notes_list_project_error_component import ApiV1NotesListProjectErrorComponent
        from ..models.api_v1_notes_list_search_error_component import ApiV1NotesListSearchErrorComponent
        from ..models.api_v1_notes_list_state_error_component import ApiV1NotesListStateErrorComponent
        from ..models.api_v1_notes_list_state_not_error_component import ApiV1NotesListStateNotErrorComponent
        from ..models.api_v1_notes_list_time_range_error_component import ApiV1NotesListTimeRangeErrorComponent
        from ..models.api_v1_notes_list_time_tracked_min_error_component import (
            ApiV1NotesListTimeTrackedMinErrorComponent,
        )
        from ..models.api_v1_notes_list_workspaces_error_component import ApiV1NotesListWorkspacesErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotesListAssignedToErrorComponent
                | ApiV1NotesListCreatedByUsersErrorComponent
                | ApiV1NotesListDatasourceErrorComponent
                | ApiV1NotesListHasTimeTrackedErrorComponent
                | ApiV1NotesListKindErrorComponent
                | ApiV1NotesListManagedByObjectIdErrorComponent
                | ApiV1NotesListNameExactErrorComponent
                | ApiV1NotesListOrganizationsErrorComponent
                | ApiV1NotesListParentNoteErrorComponent
                | ApiV1NotesListProjectErrorComponent
                | ApiV1NotesListSearchErrorComponent
                | ApiV1NotesListStateErrorComponent
                | ApiV1NotesListStateNotErrorComponent
                | ApiV1NotesListTimeRangeErrorComponent
                | ApiV1NotesListTimeTrackedMinErrorComponent
                | ApiV1NotesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_0 = ApiV1NotesListSearchErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_1 = ApiV1NotesListTimeRangeErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_2 = (
                        ApiV1NotesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_3 = ApiV1NotesListWorkspacesErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_4 = ApiV1NotesListStateErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_notes_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_5 = ApiV1NotesListKindErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_notes_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_6 = (
                        ApiV1NotesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_7 = ApiV1NotesListAssignedToErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_8 = ApiV1NotesListDatasourceErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_9 = (
                        ApiV1NotesListManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_10 = (
                        ApiV1NotesListParentNoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_11 = ApiV1NotesListProjectErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_12 = (
                        ApiV1NotesListHasTimeTrackedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_13 = (
                        ApiV1NotesListTimeTrackedMinErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_list_error_type_14 = ApiV1NotesListStateNotErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notes_list_error_type_15 = ApiV1NotesListNameExactErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_notes_list_error_type_15

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notes_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notes_list_validation_error.additional_properties = d
        return api_v1_notes_list_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
