from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_organizations_choices_list_created_by_users_error_component import (
        ApiV1OrganizationsChoicesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_endpoint_monitoring_mode_error_component import (
        ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_grafana_dashboard_error_component import (
        ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_kind_error_component import (
        ApiV1OrganizationsChoicesListKindErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_legal_name_error_component import (
        ApiV1OrganizationsChoicesListLegalNameErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_name_exact_error_component import (
        ApiV1OrganizationsChoicesListNameExactErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_search_error_component import (
        ApiV1OrganizationsChoicesListSearchErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_slug_error_component import (
        ApiV1OrganizationsChoicesListSlugErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_state_error_component import (
        ApiV1OrganizationsChoicesListStateErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_state_not_error_component import (
        ApiV1OrganizationsChoicesListStateNotErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_time_range_error_component import (
        ApiV1OrganizationsChoicesListTimeRangeErrorComponent,
    )
    from ..models.api_v1_organizations_choices_list_workspaces_error_component import (
        ApiV1OrganizationsChoicesListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1OrganizationsChoicesListValidationError")


@_attrs_define
class ApiV1OrganizationsChoicesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1OrganizationsChoicesListCreatedByUsersErrorComponent |
            ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponent |
            ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponent | ApiV1OrganizationsChoicesListKindErrorComponent |
            ApiV1OrganizationsChoicesListLegalNameErrorComponent | ApiV1OrganizationsChoicesListNameExactErrorComponent |
            ApiV1OrganizationsChoicesListSearchErrorComponent | ApiV1OrganizationsChoicesListSlugErrorComponent |
            ApiV1OrganizationsChoicesListStateErrorComponent | ApiV1OrganizationsChoicesListStateNotErrorComponent |
            ApiV1OrganizationsChoicesListTimeRangeErrorComponent | ApiV1OrganizationsChoicesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1OrganizationsChoicesListCreatedByUsersErrorComponent
        | ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponent
        | ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponent
        | ApiV1OrganizationsChoicesListKindErrorComponent
        | ApiV1OrganizationsChoicesListLegalNameErrorComponent
        | ApiV1OrganizationsChoicesListNameExactErrorComponent
        | ApiV1OrganizationsChoicesListSearchErrorComponent
        | ApiV1OrganizationsChoicesListSlugErrorComponent
        | ApiV1OrganizationsChoicesListStateErrorComponent
        | ApiV1OrganizationsChoicesListStateNotErrorComponent
        | ApiV1OrganizationsChoicesListTimeRangeErrorComponent
        | ApiV1OrganizationsChoicesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_organizations_choices_list_created_by_users_error_component import (
            ApiV1OrganizationsChoicesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_grafana_dashboard_error_component import (
            ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_kind_error_component import (
            ApiV1OrganizationsChoicesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_legal_name_error_component import (
            ApiV1OrganizationsChoicesListLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_search_error_component import (
            ApiV1OrganizationsChoicesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_slug_error_component import (
            ApiV1OrganizationsChoicesListSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_state_error_component import (
            ApiV1OrganizationsChoicesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_state_not_error_component import (
            ApiV1OrganizationsChoicesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_time_range_error_component import (
            ApiV1OrganizationsChoicesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_workspaces_error_component import (
            ApiV1OrganizationsChoicesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1OrganizationsChoicesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsChoicesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsChoicesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsChoicesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsChoicesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsChoicesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsChoicesListSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsChoicesListLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsChoicesListStateNotErrorComponent):
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
        from ..models.api_v1_organizations_choices_list_created_by_users_error_component import (
            ApiV1OrganizationsChoicesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_grafana_dashboard_error_component import (
            ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_kind_error_component import (
            ApiV1OrganizationsChoicesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_legal_name_error_component import (
            ApiV1OrganizationsChoicesListLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_name_exact_error_component import (
            ApiV1OrganizationsChoicesListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_search_error_component import (
            ApiV1OrganizationsChoicesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_slug_error_component import (
            ApiV1OrganizationsChoicesListSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_state_error_component import (
            ApiV1OrganizationsChoicesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_state_not_error_component import (
            ApiV1OrganizationsChoicesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_time_range_error_component import (
            ApiV1OrganizationsChoicesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_choices_list_workspaces_error_component import (
            ApiV1OrganizationsChoicesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1OrganizationsChoicesListCreatedByUsersErrorComponent
                | ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponent
                | ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponent
                | ApiV1OrganizationsChoicesListKindErrorComponent
                | ApiV1OrganizationsChoicesListLegalNameErrorComponent
                | ApiV1OrganizationsChoicesListNameExactErrorComponent
                | ApiV1OrganizationsChoicesListSearchErrorComponent
                | ApiV1OrganizationsChoicesListSlugErrorComponent
                | ApiV1OrganizationsChoicesListStateErrorComponent
                | ApiV1OrganizationsChoicesListStateNotErrorComponent
                | ApiV1OrganizationsChoicesListTimeRangeErrorComponent
                | ApiV1OrganizationsChoicesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_0 = (
                        ApiV1OrganizationsChoicesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_1 = (
                        ApiV1OrganizationsChoicesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_2 = (
                        ApiV1OrganizationsChoicesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_3 = (
                        ApiV1OrganizationsChoicesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_4 = (
                        ApiV1OrganizationsChoicesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_5 = (
                        ApiV1OrganizationsChoicesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_6 = (
                        ApiV1OrganizationsChoicesListSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_7 = (
                        ApiV1OrganizationsChoicesListLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_8 = (
                        ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_9 = (
                        ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_choices_list_error_type_10 = (
                        ApiV1OrganizationsChoicesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_choices_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_organizations_choices_list_error_type_11 = (
                    ApiV1OrganizationsChoicesListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_organizations_choices_list_error_type_11

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_organizations_choices_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_organizations_choices_list_validation_error.additional_properties = d
        return api_v1_organizations_choices_list_validation_error

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
