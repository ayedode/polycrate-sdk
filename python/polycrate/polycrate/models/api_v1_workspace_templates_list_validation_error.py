from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspace_templates_list_created_by_users_error_component import (
        ApiV1WorkspaceTemplatesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_workspace_templates_list_kind_error_component import (
        ApiV1WorkspaceTemplatesListKindErrorComponent,
    )
    from ..models.api_v1_workspace_templates_list_name_exact_error_component import (
        ApiV1WorkspaceTemplatesListNameExactErrorComponent,
    )
    from ..models.api_v1_workspace_templates_list_organizations_error_component import (
        ApiV1WorkspaceTemplatesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_workspace_templates_list_search_error_component import (
        ApiV1WorkspaceTemplatesListSearchErrorComponent,
    )
    from ..models.api_v1_workspace_templates_list_state_error_component import (
        ApiV1WorkspaceTemplatesListStateErrorComponent,
    )
    from ..models.api_v1_workspace_templates_list_state_not_error_component import (
        ApiV1WorkspaceTemplatesListStateNotErrorComponent,
    )
    from ..models.api_v1_workspace_templates_list_time_range_error_component import (
        ApiV1WorkspaceTemplatesListTimeRangeErrorComponent,
    )
    from ..models.api_v1_workspace_templates_list_workspaces_error_component import (
        ApiV1WorkspaceTemplatesListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspaceTemplatesListValidationError")


@_attrs_define
class ApiV1WorkspaceTemplatesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspaceTemplatesListCreatedByUsersErrorComponent |
            ApiV1WorkspaceTemplatesListKindErrorComponent | ApiV1WorkspaceTemplatesListNameExactErrorComponent |
            ApiV1WorkspaceTemplatesListOrganizationsErrorComponent | ApiV1WorkspaceTemplatesListSearchErrorComponent |
            ApiV1WorkspaceTemplatesListStateErrorComponent | ApiV1WorkspaceTemplatesListStateNotErrorComponent |
            ApiV1WorkspaceTemplatesListTimeRangeErrorComponent | ApiV1WorkspaceTemplatesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspaceTemplatesListCreatedByUsersErrorComponent
        | ApiV1WorkspaceTemplatesListKindErrorComponent
        | ApiV1WorkspaceTemplatesListNameExactErrorComponent
        | ApiV1WorkspaceTemplatesListOrganizationsErrorComponent
        | ApiV1WorkspaceTemplatesListSearchErrorComponent
        | ApiV1WorkspaceTemplatesListStateErrorComponent
        | ApiV1WorkspaceTemplatesListStateNotErrorComponent
        | ApiV1WorkspaceTemplatesListTimeRangeErrorComponent
        | ApiV1WorkspaceTemplatesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspace_templates_list_created_by_users_error_component import (
            ApiV1WorkspaceTemplatesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_kind_error_component import (
            ApiV1WorkspaceTemplatesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_organizations_error_component import (
            ApiV1WorkspaceTemplatesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_search_error_component import (
            ApiV1WorkspaceTemplatesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_state_error_component import (
            ApiV1WorkspaceTemplatesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_state_not_error_component import (
            ApiV1WorkspaceTemplatesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_time_range_error_component import (
            ApiV1WorkspaceTemplatesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_workspaces_error_component import (
            ApiV1WorkspaceTemplatesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspaceTemplatesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesListStateNotErrorComponent):
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
        from ..models.api_v1_workspace_templates_list_created_by_users_error_component import (
            ApiV1WorkspaceTemplatesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_kind_error_component import (
            ApiV1WorkspaceTemplatesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_name_exact_error_component import (
            ApiV1WorkspaceTemplatesListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_organizations_error_component import (
            ApiV1WorkspaceTemplatesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_search_error_component import (
            ApiV1WorkspaceTemplatesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_state_error_component import (
            ApiV1WorkspaceTemplatesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_state_not_error_component import (
            ApiV1WorkspaceTemplatesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_time_range_error_component import (
            ApiV1WorkspaceTemplatesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_list_workspaces_error_component import (
            ApiV1WorkspaceTemplatesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspaceTemplatesListCreatedByUsersErrorComponent
                | ApiV1WorkspaceTemplatesListKindErrorComponent
                | ApiV1WorkspaceTemplatesListNameExactErrorComponent
                | ApiV1WorkspaceTemplatesListOrganizationsErrorComponent
                | ApiV1WorkspaceTemplatesListSearchErrorComponent
                | ApiV1WorkspaceTemplatesListStateErrorComponent
                | ApiV1WorkspaceTemplatesListStateNotErrorComponent
                | ApiV1WorkspaceTemplatesListTimeRangeErrorComponent
                | ApiV1WorkspaceTemplatesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_list_error_type_0 = (
                        ApiV1WorkspaceTemplatesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_list_error_type_1 = (
                        ApiV1WorkspaceTemplatesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_list_error_type_2 = (
                        ApiV1WorkspaceTemplatesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_list_error_type_3 = (
                        ApiV1WorkspaceTemplatesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_list_error_type_4 = (
                        ApiV1WorkspaceTemplatesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_list_error_type_5 = (
                        ApiV1WorkspaceTemplatesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_list_error_type_6 = (
                        ApiV1WorkspaceTemplatesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_list_error_type_7 = (
                        ApiV1WorkspaceTemplatesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspace_templates_list_error_type_8 = (
                    ApiV1WorkspaceTemplatesListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspace_templates_list_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspace_templates_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspace_templates_list_validation_error.additional_properties = d
        return api_v1_workspace_templates_list_validation_error

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
