from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_activities_list_created_by_users_error_component import (
        ApiV1ActivitiesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_activities_list_kind_error_component import ApiV1ActivitiesListKindErrorComponent
    from ..models.api_v1_activities_list_name_exact_error_component import ApiV1ActivitiesListNameExactErrorComponent
    from ..models.api_v1_activities_list_object_id_error_component import ApiV1ActivitiesListObjectIdErrorComponent
    from ..models.api_v1_activities_list_object_type_error_component import ApiV1ActivitiesListObjectTypeErrorComponent
    from ..models.api_v1_activities_list_organizations_error_component import (
        ApiV1ActivitiesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_activities_list_search_error_component import ApiV1ActivitiesListSearchErrorComponent
    from ..models.api_v1_activities_list_state_error_component import ApiV1ActivitiesListStateErrorComponent
    from ..models.api_v1_activities_list_state_not_error_component import ApiV1ActivitiesListStateNotErrorComponent
    from ..models.api_v1_activities_list_time_range_error_component import ApiV1ActivitiesListTimeRangeErrorComponent
    from ..models.api_v1_activities_list_user_error_component import ApiV1ActivitiesListUserErrorComponent
    from ..models.api_v1_activities_list_workspaces_error_component import ApiV1ActivitiesListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1ActivitiesListValidationError")


@_attrs_define
class ApiV1ActivitiesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ActivitiesListCreatedByUsersErrorComponent | ApiV1ActivitiesListKindErrorComponent |
            ApiV1ActivitiesListNameExactErrorComponent | ApiV1ActivitiesListObjectIdErrorComponent |
            ApiV1ActivitiesListObjectTypeErrorComponent | ApiV1ActivitiesListOrganizationsErrorComponent |
            ApiV1ActivitiesListSearchErrorComponent | ApiV1ActivitiesListStateErrorComponent |
            ApiV1ActivitiesListStateNotErrorComponent | ApiV1ActivitiesListTimeRangeErrorComponent |
            ApiV1ActivitiesListUserErrorComponent | ApiV1ActivitiesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ActivitiesListCreatedByUsersErrorComponent
        | ApiV1ActivitiesListKindErrorComponent
        | ApiV1ActivitiesListNameExactErrorComponent
        | ApiV1ActivitiesListObjectIdErrorComponent
        | ApiV1ActivitiesListObjectTypeErrorComponent
        | ApiV1ActivitiesListOrganizationsErrorComponent
        | ApiV1ActivitiesListSearchErrorComponent
        | ApiV1ActivitiesListStateErrorComponent
        | ApiV1ActivitiesListStateNotErrorComponent
        | ApiV1ActivitiesListTimeRangeErrorComponent
        | ApiV1ActivitiesListUserErrorComponent
        | ApiV1ActivitiesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_activities_list_created_by_users_error_component import (
            ApiV1ActivitiesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_kind_error_component import (
            ApiV1ActivitiesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_object_id_error_component import (
            ApiV1ActivitiesListObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_object_type_error_component import (
            ApiV1ActivitiesListObjectTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_organizations_error_component import (
            ApiV1ActivitiesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_search_error_component import (
            ApiV1ActivitiesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_state_error_component import (
            ApiV1ActivitiesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_state_not_error_component import (
            ApiV1ActivitiesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_time_range_error_component import (
            ApiV1ActivitiesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_user_error_component import (
            ApiV1ActivitiesListUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_workspaces_error_component import (
            ApiV1ActivitiesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ActivitiesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActivitiesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActivitiesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActivitiesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActivitiesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActivitiesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActivitiesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActivitiesListUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActivitiesListObjectTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActivitiesListObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActivitiesListStateNotErrorComponent):
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
        from ..models.api_v1_activities_list_created_by_users_error_component import (
            ApiV1ActivitiesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_kind_error_component import (
            ApiV1ActivitiesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_name_exact_error_component import (
            ApiV1ActivitiesListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_object_id_error_component import (
            ApiV1ActivitiesListObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_object_type_error_component import (
            ApiV1ActivitiesListObjectTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_organizations_error_component import (
            ApiV1ActivitiesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_search_error_component import (
            ApiV1ActivitiesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_state_error_component import (
            ApiV1ActivitiesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_state_not_error_component import (
            ApiV1ActivitiesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_time_range_error_component import (
            ApiV1ActivitiesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_user_error_component import (
            ApiV1ActivitiesListUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_activities_list_workspaces_error_component import (
            ApiV1ActivitiesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ActivitiesListCreatedByUsersErrorComponent
                | ApiV1ActivitiesListKindErrorComponent
                | ApiV1ActivitiesListNameExactErrorComponent
                | ApiV1ActivitiesListObjectIdErrorComponent
                | ApiV1ActivitiesListObjectTypeErrorComponent
                | ApiV1ActivitiesListOrganizationsErrorComponent
                | ApiV1ActivitiesListSearchErrorComponent
                | ApiV1ActivitiesListStateErrorComponent
                | ApiV1ActivitiesListStateNotErrorComponent
                | ApiV1ActivitiesListTimeRangeErrorComponent
                | ApiV1ActivitiesListUserErrorComponent
                | ApiV1ActivitiesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_0 = (
                        ApiV1ActivitiesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_1 = (
                        ApiV1ActivitiesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_2 = (
                        ApiV1ActivitiesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_3 = (
                        ApiV1ActivitiesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_4 = (
                        ApiV1ActivitiesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_5 = (
                        ApiV1ActivitiesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_6 = (
                        ApiV1ActivitiesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_7 = (
                        ApiV1ActivitiesListUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_8 = (
                        ApiV1ActivitiesListObjectTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_9 = (
                        ApiV1ActivitiesListObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_activities_list_error_type_10 = (
                        ApiV1ActivitiesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_activities_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_activities_list_error_type_11 = (
                    ApiV1ActivitiesListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_activities_list_error_type_11

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_activities_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_activities_list_validation_error.additional_properties = d
        return api_v1_activities_list_validation_error

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
