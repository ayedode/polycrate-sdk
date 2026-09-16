from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_agents_list_created_by_users_error_component import ApiV1AgentsListCreatedByUsersErrorComponent
    from ..models.api_v1_agents_list_kind_error_component import ApiV1AgentsListKindErrorComponent
    from ..models.api_v1_agents_list_name_exact_error_component import ApiV1AgentsListNameExactErrorComponent
    from ..models.api_v1_agents_list_organizations_error_component import ApiV1AgentsListOrganizationsErrorComponent
    from ..models.api_v1_agents_list_pops_error_component import ApiV1AgentsListPopsErrorComponent
    from ..models.api_v1_agents_list_search_error_component import ApiV1AgentsListSearchErrorComponent
    from ..models.api_v1_agents_list_state_error_component import ApiV1AgentsListStateErrorComponent
    from ..models.api_v1_agents_list_state_not_error_component import ApiV1AgentsListStateNotErrorComponent
    from ..models.api_v1_agents_list_time_range_error_component import ApiV1AgentsListTimeRangeErrorComponent
    from ..models.api_v1_agents_list_version_error_component import ApiV1AgentsListVersionErrorComponent
    from ..models.api_v1_agents_list_workspaces_error_component import ApiV1AgentsListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1AgentsListValidationError")


@_attrs_define
class ApiV1AgentsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AgentsListCreatedByUsersErrorComponent | ApiV1AgentsListKindErrorComponent |
            ApiV1AgentsListNameExactErrorComponent | ApiV1AgentsListOrganizationsErrorComponent |
            ApiV1AgentsListPopsErrorComponent | ApiV1AgentsListSearchErrorComponent | ApiV1AgentsListStateErrorComponent |
            ApiV1AgentsListStateNotErrorComponent | ApiV1AgentsListTimeRangeErrorComponent |
            ApiV1AgentsListVersionErrorComponent | ApiV1AgentsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AgentsListCreatedByUsersErrorComponent
        | ApiV1AgentsListKindErrorComponent
        | ApiV1AgentsListNameExactErrorComponent
        | ApiV1AgentsListOrganizationsErrorComponent
        | ApiV1AgentsListPopsErrorComponent
        | ApiV1AgentsListSearchErrorComponent
        | ApiV1AgentsListStateErrorComponent
        | ApiV1AgentsListStateNotErrorComponent
        | ApiV1AgentsListTimeRangeErrorComponent
        | ApiV1AgentsListVersionErrorComponent
        | ApiV1AgentsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_agents_list_created_by_users_error_component import (
            ApiV1AgentsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_kind_error_component import ApiV1AgentsListKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_agents_list_organizations_error_component import (
            ApiV1AgentsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_pops_error_component import ApiV1AgentsListPopsErrorComponent  # noqa: PLC0415
        from ..models.api_v1_agents_list_search_error_component import (
            ApiV1AgentsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_state_error_component import (
            ApiV1AgentsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_state_not_error_component import (
            ApiV1AgentsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_time_range_error_component import (
            ApiV1AgentsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_version_error_component import (
            ApiV1AgentsListVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_workspaces_error_component import (
            ApiV1AgentsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AgentsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AgentsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AgentsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AgentsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AgentsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AgentsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AgentsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AgentsListPopsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AgentsListVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AgentsListStateNotErrorComponent):
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
        from ..models.api_v1_agents_list_created_by_users_error_component import (
            ApiV1AgentsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_kind_error_component import ApiV1AgentsListKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_agents_list_name_exact_error_component import (
            ApiV1AgentsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_organizations_error_component import (
            ApiV1AgentsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_pops_error_component import ApiV1AgentsListPopsErrorComponent  # noqa: PLC0415
        from ..models.api_v1_agents_list_search_error_component import (
            ApiV1AgentsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_state_error_component import (
            ApiV1AgentsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_state_not_error_component import (
            ApiV1AgentsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_time_range_error_component import (
            ApiV1AgentsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_version_error_component import (
            ApiV1AgentsListVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_agents_list_workspaces_error_component import (
            ApiV1AgentsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AgentsListCreatedByUsersErrorComponent
                | ApiV1AgentsListKindErrorComponent
                | ApiV1AgentsListNameExactErrorComponent
                | ApiV1AgentsListOrganizationsErrorComponent
                | ApiV1AgentsListPopsErrorComponent
                | ApiV1AgentsListSearchErrorComponent
                | ApiV1AgentsListStateErrorComponent
                | ApiV1AgentsListStateNotErrorComponent
                | ApiV1AgentsListTimeRangeErrorComponent
                | ApiV1AgentsListVersionErrorComponent
                | ApiV1AgentsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_agents_list_error_type_0 = ApiV1AgentsListSearchErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_agents_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_agents_list_error_type_1 = (
                        ApiV1AgentsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_agents_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_agents_list_error_type_2 = (
                        ApiV1AgentsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_agents_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_agents_list_error_type_3 = (
                        ApiV1AgentsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_agents_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_agents_list_error_type_4 = ApiV1AgentsListStateErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_agents_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_agents_list_error_type_5 = ApiV1AgentsListKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_agents_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_agents_list_error_type_6 = (
                        ApiV1AgentsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_agents_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_agents_list_error_type_7 = ApiV1AgentsListPopsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_agents_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_agents_list_error_type_8 = ApiV1AgentsListVersionErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_agents_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_agents_list_error_type_9 = ApiV1AgentsListStateNotErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_agents_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_agents_list_error_type_10 = ApiV1AgentsListNameExactErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_agents_list_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_agents_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_agents_list_validation_error.additional_properties = d
        return api_v1_agents_list_validation_error

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
