from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_downtimes_list_created_by_users_error_component import (
        ApiV1DowntimesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_downtimes_list_endpoints_error_component import ApiV1DowntimesListEndpointsErrorComponent
    from ..models.api_v1_downtimes_list_incidents_error_component import ApiV1DowntimesListIncidentsErrorComponent
    from ..models.api_v1_downtimes_list_kind_error_component import ApiV1DowntimesListKindErrorComponent
    from ..models.api_v1_downtimes_list_kubernetes_apps_error_component import (
        ApiV1DowntimesListKubernetesAppsErrorComponent,
    )
    from ..models.api_v1_downtimes_list_kubernetes_clusters_error_component import (
        ApiV1DowntimesListKubernetesClustersErrorComponent,
    )
    from ..models.api_v1_downtimes_list_name_exact_error_component import ApiV1DowntimesListNameExactErrorComponent
    from ..models.api_v1_downtimes_list_organizations_error_component import (
        ApiV1DowntimesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_downtimes_list_search_error_component import ApiV1DowntimesListSearchErrorComponent
    from ..models.api_v1_downtimes_list_since_error_component import ApiV1DowntimesListSinceErrorComponent
    from ..models.api_v1_downtimes_list_state_error_component import ApiV1DowntimesListStateErrorComponent
    from ..models.api_v1_downtimes_list_state_not_error_component import ApiV1DowntimesListStateNotErrorComponent
    from ..models.api_v1_downtimes_list_time_range_error_component import ApiV1DowntimesListTimeRangeErrorComponent
    from ..models.api_v1_downtimes_list_until_error_component import ApiV1DowntimesListUntilErrorComponent
    from ..models.api_v1_downtimes_list_workspaces_error_component import ApiV1DowntimesListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1DowntimesListValidationError")


@_attrs_define
class ApiV1DowntimesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DowntimesListCreatedByUsersErrorComponent | ApiV1DowntimesListEndpointsErrorComponent |
            ApiV1DowntimesListIncidentsErrorComponent | ApiV1DowntimesListKindErrorComponent |
            ApiV1DowntimesListKubernetesAppsErrorComponent | ApiV1DowntimesListKubernetesClustersErrorComponent |
            ApiV1DowntimesListNameExactErrorComponent | ApiV1DowntimesListOrganizationsErrorComponent |
            ApiV1DowntimesListSearchErrorComponent | ApiV1DowntimesListSinceErrorComponent |
            ApiV1DowntimesListStateErrorComponent | ApiV1DowntimesListStateNotErrorComponent |
            ApiV1DowntimesListTimeRangeErrorComponent | ApiV1DowntimesListUntilErrorComponent |
            ApiV1DowntimesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DowntimesListCreatedByUsersErrorComponent
        | ApiV1DowntimesListEndpointsErrorComponent
        | ApiV1DowntimesListIncidentsErrorComponent
        | ApiV1DowntimesListKindErrorComponent
        | ApiV1DowntimesListKubernetesAppsErrorComponent
        | ApiV1DowntimesListKubernetesClustersErrorComponent
        | ApiV1DowntimesListNameExactErrorComponent
        | ApiV1DowntimesListOrganizationsErrorComponent
        | ApiV1DowntimesListSearchErrorComponent
        | ApiV1DowntimesListSinceErrorComponent
        | ApiV1DowntimesListStateErrorComponent
        | ApiV1DowntimesListStateNotErrorComponent
        | ApiV1DowntimesListTimeRangeErrorComponent
        | ApiV1DowntimesListUntilErrorComponent
        | ApiV1DowntimesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_downtimes_list_created_by_users_error_component import (
            ApiV1DowntimesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_endpoints_error_component import (
            ApiV1DowntimesListEndpointsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_incidents_error_component import (
            ApiV1DowntimesListIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_kind_error_component import (
            ApiV1DowntimesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_kubernetes_apps_error_component import (
            ApiV1DowntimesListKubernetesAppsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_kubernetes_clusters_error_component import (
            ApiV1DowntimesListKubernetesClustersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_organizations_error_component import (
            ApiV1DowntimesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_search_error_component import (
            ApiV1DowntimesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_since_error_component import (
            ApiV1DowntimesListSinceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_state_error_component import (
            ApiV1DowntimesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_state_not_error_component import (
            ApiV1DowntimesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_time_range_error_component import (
            ApiV1DowntimesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_until_error_component import (
            ApiV1DowntimesListUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_workspaces_error_component import (
            ApiV1DowntimesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DowntimesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListKubernetesAppsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListKubernetesClustersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListEndpointsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListIncidentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListSinceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesListStateNotErrorComponent):
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
        from ..models.api_v1_downtimes_list_created_by_users_error_component import (
            ApiV1DowntimesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_endpoints_error_component import (
            ApiV1DowntimesListEndpointsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_incidents_error_component import (
            ApiV1DowntimesListIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_kind_error_component import (
            ApiV1DowntimesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_kubernetes_apps_error_component import (
            ApiV1DowntimesListKubernetesAppsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_kubernetes_clusters_error_component import (
            ApiV1DowntimesListKubernetesClustersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_name_exact_error_component import (
            ApiV1DowntimesListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_organizations_error_component import (
            ApiV1DowntimesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_search_error_component import (
            ApiV1DowntimesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_since_error_component import (
            ApiV1DowntimesListSinceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_state_error_component import (
            ApiV1DowntimesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_state_not_error_component import (
            ApiV1DowntimesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_time_range_error_component import (
            ApiV1DowntimesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_until_error_component import (
            ApiV1DowntimesListUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_list_workspaces_error_component import (
            ApiV1DowntimesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DowntimesListCreatedByUsersErrorComponent
                | ApiV1DowntimesListEndpointsErrorComponent
                | ApiV1DowntimesListIncidentsErrorComponent
                | ApiV1DowntimesListKindErrorComponent
                | ApiV1DowntimesListKubernetesAppsErrorComponent
                | ApiV1DowntimesListKubernetesClustersErrorComponent
                | ApiV1DowntimesListNameExactErrorComponent
                | ApiV1DowntimesListOrganizationsErrorComponent
                | ApiV1DowntimesListSearchErrorComponent
                | ApiV1DowntimesListSinceErrorComponent
                | ApiV1DowntimesListStateErrorComponent
                | ApiV1DowntimesListStateNotErrorComponent
                | ApiV1DowntimesListTimeRangeErrorComponent
                | ApiV1DowntimesListUntilErrorComponent
                | ApiV1DowntimesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_0 = (
                        ApiV1DowntimesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_1 = (
                        ApiV1DowntimesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_2 = (
                        ApiV1DowntimesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_3 = (
                        ApiV1DowntimesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_4 = (
                        ApiV1DowntimesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_5 = (
                        ApiV1DowntimesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_6 = (
                        ApiV1DowntimesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_7 = (
                        ApiV1DowntimesListKubernetesAppsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_8 = (
                        ApiV1DowntimesListKubernetesClustersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_9 = (
                        ApiV1DowntimesListEndpointsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_10 = (
                        ApiV1DowntimesListIncidentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_11 = (
                        ApiV1DowntimesListSinceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_12 = (
                        ApiV1DowntimesListUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_list_error_type_13 = (
                        ApiV1DowntimesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_downtimes_list_error_type_14 = (
                    ApiV1DowntimesListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_downtimes_list_error_type_14

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_downtimes_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_downtimes_list_validation_error.additional_properties = d
        return api_v1_downtimes_list_validation_error

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
