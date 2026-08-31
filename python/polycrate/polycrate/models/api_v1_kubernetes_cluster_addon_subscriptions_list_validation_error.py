from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_addon_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_created_at_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_created_by_component_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_created_by_users_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_k8s_cluster_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_kind_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_name_exact_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListNameExactErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_organizations_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_scope_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_search_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_state_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_state_not_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_time_range_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_updated_at_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_version_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_workspaces_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClusterAddonSubscriptionsListValidationError")


@_attrs_define
class ApiV1KubernetesClusterAddonSubscriptionsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListCreatedByComponentErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListCreatedByUsersErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListK8SClusterErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListNameExactErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListOrganizationsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListUpdatedAtErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListCreatedByComponentErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListCreatedByUsersErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListK8SClusterErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListNameExactErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListOrganizationsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListUpdatedAtErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_addon_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_created_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_created_by_component_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_created_by_users_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_k8s_cluster_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_kind_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_organizations_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_scope_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_search_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_state_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_state_not_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_time_range_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_updated_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_version_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_workspaces_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListCreatedByComponentErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponent):
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
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_addon_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_created_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_created_by_component_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_created_by_users_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_k8s_cluster_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_kind_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_name_exact_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListNameExactErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_organizations_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_scope_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_search_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_state_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_state_not_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_time_range_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_updated_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_version_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_list_workspaces_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListCreatedByComponentErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListCreatedByUsersErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListK8SClusterErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListNameExactErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListOrganizationsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListUpdatedAtErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_0 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_1 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_2 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_3 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_4 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_5 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_6 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_7 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_8 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_9 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_10 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_11 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_12 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_13 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_14 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_15 = (
                        ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_16 = (
                    ApiV1KubernetesClusterAddonSubscriptionsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_list_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_cluster_addon_subscriptions_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_cluster_addon_subscriptions_list_validation_error.additional_properties = d
        return api_v1_kubernetes_cluster_addon_subscriptions_list_validation_error

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
