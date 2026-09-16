from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_action_runs_list_action_error_component import ApiV1ActionRunsListActionErrorComponent
    from ..models.api_v1_action_runs_list_blocks_error_component import ApiV1ActionRunsListBlocksErrorComponent
    from ..models.api_v1_action_runs_list_created_by_users_error_component import (
        ApiV1ActionRunsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_action_runs_list_kind_error_component import ApiV1ActionRunsListKindErrorComponent
    from ..models.api_v1_action_runs_list_name_exact_error_component import ApiV1ActionRunsListNameExactErrorComponent
    from ..models.api_v1_action_runs_list_organizations_error_component import (
        ApiV1ActionRunsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_action_runs_list_search_error_component import ApiV1ActionRunsListSearchErrorComponent
    from ..models.api_v1_action_runs_list_state_error_component import ApiV1ActionRunsListStateErrorComponent
    from ..models.api_v1_action_runs_list_state_not_error_component import ApiV1ActionRunsListStateNotErrorComponent
    from ..models.api_v1_action_runs_list_status_error_component import ApiV1ActionRunsListStatusErrorComponent
    from ..models.api_v1_action_runs_list_time_range_error_component import ApiV1ActionRunsListTimeRangeErrorComponent
    from ..models.api_v1_action_runs_list_workspaces_error_component import ApiV1ActionRunsListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1ActionRunsListValidationError")


@_attrs_define
class ApiV1ActionRunsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ActionRunsListActionErrorComponent | ApiV1ActionRunsListBlocksErrorComponent |
            ApiV1ActionRunsListCreatedByUsersErrorComponent | ApiV1ActionRunsListKindErrorComponent |
            ApiV1ActionRunsListNameExactErrorComponent | ApiV1ActionRunsListOrganizationsErrorComponent |
            ApiV1ActionRunsListSearchErrorComponent | ApiV1ActionRunsListStateErrorComponent |
            ApiV1ActionRunsListStateNotErrorComponent | ApiV1ActionRunsListStatusErrorComponent |
            ApiV1ActionRunsListTimeRangeErrorComponent | ApiV1ActionRunsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ActionRunsListActionErrorComponent
        | ApiV1ActionRunsListBlocksErrorComponent
        | ApiV1ActionRunsListCreatedByUsersErrorComponent
        | ApiV1ActionRunsListKindErrorComponent
        | ApiV1ActionRunsListNameExactErrorComponent
        | ApiV1ActionRunsListOrganizationsErrorComponent
        | ApiV1ActionRunsListSearchErrorComponent
        | ApiV1ActionRunsListStateErrorComponent
        | ApiV1ActionRunsListStateNotErrorComponent
        | ApiV1ActionRunsListStatusErrorComponent
        | ApiV1ActionRunsListTimeRangeErrorComponent
        | ApiV1ActionRunsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_action_runs_list_action_error_component import (
            ApiV1ActionRunsListActionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_blocks_error_component import (
            ApiV1ActionRunsListBlocksErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_created_by_users_error_component import (
            ApiV1ActionRunsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_kind_error_component import (
            ApiV1ActionRunsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_organizations_error_component import (
            ApiV1ActionRunsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_search_error_component import (
            ApiV1ActionRunsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_state_error_component import (
            ApiV1ActionRunsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_state_not_error_component import (
            ApiV1ActionRunsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_status_error_component import (
            ApiV1ActionRunsListStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_time_range_error_component import (
            ApiV1ActionRunsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_workspaces_error_component import (
            ApiV1ActionRunsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ActionRunsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActionRunsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActionRunsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActionRunsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActionRunsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActionRunsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActionRunsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActionRunsListBlocksErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActionRunsListStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActionRunsListActionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ActionRunsListStateNotErrorComponent):
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
        from ..models.api_v1_action_runs_list_action_error_component import (
            ApiV1ActionRunsListActionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_blocks_error_component import (
            ApiV1ActionRunsListBlocksErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_created_by_users_error_component import (
            ApiV1ActionRunsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_kind_error_component import (
            ApiV1ActionRunsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_name_exact_error_component import (
            ApiV1ActionRunsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_organizations_error_component import (
            ApiV1ActionRunsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_search_error_component import (
            ApiV1ActionRunsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_state_error_component import (
            ApiV1ActionRunsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_state_not_error_component import (
            ApiV1ActionRunsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_status_error_component import (
            ApiV1ActionRunsListStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_time_range_error_component import (
            ApiV1ActionRunsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_action_runs_list_workspaces_error_component import (
            ApiV1ActionRunsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ActionRunsListActionErrorComponent
                | ApiV1ActionRunsListBlocksErrorComponent
                | ApiV1ActionRunsListCreatedByUsersErrorComponent
                | ApiV1ActionRunsListKindErrorComponent
                | ApiV1ActionRunsListNameExactErrorComponent
                | ApiV1ActionRunsListOrganizationsErrorComponent
                | ApiV1ActionRunsListSearchErrorComponent
                | ApiV1ActionRunsListStateErrorComponent
                | ApiV1ActionRunsListStateNotErrorComponent
                | ApiV1ActionRunsListStatusErrorComponent
                | ApiV1ActionRunsListTimeRangeErrorComponent
                | ApiV1ActionRunsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_0 = (
                        ApiV1ActionRunsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_1 = (
                        ApiV1ActionRunsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_2 = (
                        ApiV1ActionRunsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_3 = (
                        ApiV1ActionRunsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_4 = (
                        ApiV1ActionRunsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_5 = (
                        ApiV1ActionRunsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_6 = (
                        ApiV1ActionRunsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_7 = (
                        ApiV1ActionRunsListBlocksErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_8 = (
                        ApiV1ActionRunsListStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_9 = (
                        ApiV1ActionRunsListActionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_action_runs_list_error_type_10 = (
                        ApiV1ActionRunsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_action_runs_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_action_runs_list_error_type_11 = (
                    ApiV1ActionRunsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_action_runs_list_error_type_11

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_action_runs_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_action_runs_list_validation_error.additional_properties = d
        return api_v1_action_runs_list_validation_error

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
