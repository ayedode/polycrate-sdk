from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_apps_list_catalogue_app_error_component import (
        ApiV1KubernetesAppsListCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_created_at_error_component import (
        ApiV1KubernetesAppsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_created_by_component_error_component import (
        ApiV1KubernetesAppsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_created_by_users_error_component import (
        ApiV1KubernetesAppsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_helm_chart_error_component import (
        ApiV1KubernetesAppsListHelmChartErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_k8s_cluster_error_component import (
        ApiV1KubernetesAppsListK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_kind_error_component import ApiV1KubernetesAppsListKindErrorComponent
    from ..models.api_v1_kubernetes_apps_list_name_error_component import ApiV1KubernetesAppsListNameErrorComponent
    from ..models.api_v1_kubernetes_apps_list_name_exact_error_component import (
        ApiV1KubernetesAppsListNameExactErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_organizations_error_component import (
        ApiV1KubernetesAppsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_scope_error_component import ApiV1KubernetesAppsListScopeErrorComponent
    from ..models.api_v1_kubernetes_apps_list_search_error_component import ApiV1KubernetesAppsListSearchErrorComponent
    from ..models.api_v1_kubernetes_apps_list_state_error_component import ApiV1KubernetesAppsListStateErrorComponent
    from ..models.api_v1_kubernetes_apps_list_state_not_error_component import (
        ApiV1KubernetesAppsListStateNotErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_time_range_error_component import (
        ApiV1KubernetesAppsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_updated_at_error_component import (
        ApiV1KubernetesAppsListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_apps_list_workspaces_error_component import (
        ApiV1KubernetesAppsListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAppsListValidationError")


@_attrs_define
class ApiV1KubernetesAppsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAppsListCatalogueAppErrorComponent | ApiV1KubernetesAppsListCreatedAtErrorComponent
            | ApiV1KubernetesAppsListCreatedByComponentErrorComponent | ApiV1KubernetesAppsListCreatedByUsersErrorComponent
            | ApiV1KubernetesAppsListHelmChartErrorComponent | ApiV1KubernetesAppsListK8SClusterErrorComponent |
            ApiV1KubernetesAppsListKindErrorComponent | ApiV1KubernetesAppsListNameErrorComponent |
            ApiV1KubernetesAppsListNameExactErrorComponent | ApiV1KubernetesAppsListOrganizationsErrorComponent |
            ApiV1KubernetesAppsListScopeErrorComponent | ApiV1KubernetesAppsListSearchErrorComponent |
            ApiV1KubernetesAppsListStateErrorComponent | ApiV1KubernetesAppsListStateNotErrorComponent |
            ApiV1KubernetesAppsListTimeRangeErrorComponent | ApiV1KubernetesAppsListUpdatedAtErrorComponent |
            ApiV1KubernetesAppsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAppsListCatalogueAppErrorComponent
        | ApiV1KubernetesAppsListCreatedAtErrorComponent
        | ApiV1KubernetesAppsListCreatedByComponentErrorComponent
        | ApiV1KubernetesAppsListCreatedByUsersErrorComponent
        | ApiV1KubernetesAppsListHelmChartErrorComponent
        | ApiV1KubernetesAppsListK8SClusterErrorComponent
        | ApiV1KubernetesAppsListKindErrorComponent
        | ApiV1KubernetesAppsListNameErrorComponent
        | ApiV1KubernetesAppsListNameExactErrorComponent
        | ApiV1KubernetesAppsListOrganizationsErrorComponent
        | ApiV1KubernetesAppsListScopeErrorComponent
        | ApiV1KubernetesAppsListSearchErrorComponent
        | ApiV1KubernetesAppsListStateErrorComponent
        | ApiV1KubernetesAppsListStateNotErrorComponent
        | ApiV1KubernetesAppsListTimeRangeErrorComponent
        | ApiV1KubernetesAppsListUpdatedAtErrorComponent
        | ApiV1KubernetesAppsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_apps_list_catalogue_app_error_component import (
            ApiV1KubernetesAppsListCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_created_at_error_component import (
            ApiV1KubernetesAppsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_created_by_component_error_component import (
            ApiV1KubernetesAppsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_created_by_users_error_component import (
            ApiV1KubernetesAppsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_helm_chart_error_component import (
            ApiV1KubernetesAppsListHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_k8s_cluster_error_component import (
            ApiV1KubernetesAppsListK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_kind_error_component import (
            ApiV1KubernetesAppsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_name_error_component import (
            ApiV1KubernetesAppsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_organizations_error_component import (
            ApiV1KubernetesAppsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_scope_error_component import (
            ApiV1KubernetesAppsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_search_error_component import (
            ApiV1KubernetesAppsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_state_error_component import (
            ApiV1KubernetesAppsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_state_not_error_component import (
            ApiV1KubernetesAppsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_time_range_error_component import (
            ApiV1KubernetesAppsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_updated_at_error_component import (
            ApiV1KubernetesAppsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_workspaces_error_component import (
            ApiV1KubernetesAppsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAppsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListHelmChartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAppsListStateNotErrorComponent):
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
        from ..models.api_v1_kubernetes_apps_list_catalogue_app_error_component import (
            ApiV1KubernetesAppsListCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_created_at_error_component import (
            ApiV1KubernetesAppsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_created_by_component_error_component import (
            ApiV1KubernetesAppsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_created_by_users_error_component import (
            ApiV1KubernetesAppsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_helm_chart_error_component import (
            ApiV1KubernetesAppsListHelmChartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_k8s_cluster_error_component import (
            ApiV1KubernetesAppsListK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_kind_error_component import (
            ApiV1KubernetesAppsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_name_error_component import (
            ApiV1KubernetesAppsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_name_exact_error_component import (
            ApiV1KubernetesAppsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_organizations_error_component import (
            ApiV1KubernetesAppsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_scope_error_component import (
            ApiV1KubernetesAppsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_search_error_component import (
            ApiV1KubernetesAppsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_state_error_component import (
            ApiV1KubernetesAppsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_state_not_error_component import (
            ApiV1KubernetesAppsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_time_range_error_component import (
            ApiV1KubernetesAppsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_updated_at_error_component import (
            ApiV1KubernetesAppsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_apps_list_workspaces_error_component import (
            ApiV1KubernetesAppsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAppsListCatalogueAppErrorComponent
                | ApiV1KubernetesAppsListCreatedAtErrorComponent
                | ApiV1KubernetesAppsListCreatedByComponentErrorComponent
                | ApiV1KubernetesAppsListCreatedByUsersErrorComponent
                | ApiV1KubernetesAppsListHelmChartErrorComponent
                | ApiV1KubernetesAppsListK8SClusterErrorComponent
                | ApiV1KubernetesAppsListKindErrorComponent
                | ApiV1KubernetesAppsListNameErrorComponent
                | ApiV1KubernetesAppsListNameExactErrorComponent
                | ApiV1KubernetesAppsListOrganizationsErrorComponent
                | ApiV1KubernetesAppsListScopeErrorComponent
                | ApiV1KubernetesAppsListSearchErrorComponent
                | ApiV1KubernetesAppsListStateErrorComponent
                | ApiV1KubernetesAppsListStateNotErrorComponent
                | ApiV1KubernetesAppsListTimeRangeErrorComponent
                | ApiV1KubernetesAppsListUpdatedAtErrorComponent
                | ApiV1KubernetesAppsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_0 = (
                        ApiV1KubernetesAppsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_1 = (
                        ApiV1KubernetesAppsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_2 = (
                        ApiV1KubernetesAppsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_3 = (
                        ApiV1KubernetesAppsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_4 = (
                        ApiV1KubernetesAppsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_5 = (
                        ApiV1KubernetesAppsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_6 = (
                        ApiV1KubernetesAppsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_7 = (
                        ApiV1KubernetesAppsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_8 = (
                        ApiV1KubernetesAppsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_9 = (
                        ApiV1KubernetesAppsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_10 = (
                        ApiV1KubernetesAppsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_11 = (
                        ApiV1KubernetesAppsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_12 = (
                        ApiV1KubernetesAppsListK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_13 = (
                        ApiV1KubernetesAppsListHelmChartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_14 = (
                        ApiV1KubernetesAppsListCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_apps_list_error_type_15 = (
                        ApiV1KubernetesAppsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_apps_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_apps_list_error_type_16 = (
                    ApiV1KubernetesAppsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_apps_list_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_apps_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_apps_list_validation_error.additional_properties = d
        return api_v1_kubernetes_apps_list_validation_error

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
