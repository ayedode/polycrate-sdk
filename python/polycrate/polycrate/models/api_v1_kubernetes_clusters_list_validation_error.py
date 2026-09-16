from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_clusters_list_created_at_error_component import (
        ApiV1KubernetesClustersListCreatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_created_by_component_error_component import (
        ApiV1KubernetesClustersListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_created_by_users_error_component import (
        ApiV1KubernetesClustersListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_kind_error_component import (
        ApiV1KubernetesClustersListKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_kubernetes_version_error_component import (
        ApiV1KubernetesClustersListKubernetesVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_name_error_component import (
        ApiV1KubernetesClustersListNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_name_exact_error_component import (
        ApiV1KubernetesClustersListNameExactErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_organizations_error_component import (
        ApiV1KubernetesClustersListOrganizationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_scope_error_component import (
        ApiV1KubernetesClustersListScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_search_error_component import (
        ApiV1KubernetesClustersListSearchErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_state_error_component import (
        ApiV1KubernetesClustersListStateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_state_not_error_component import (
        ApiV1KubernetesClustersListStateNotErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_time_range_error_component import (
        ApiV1KubernetesClustersListTimeRangeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_updated_at_error_component import (
        ApiV1KubernetesClustersListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_list_workspaces_error_component import (
        ApiV1KubernetesClustersListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClustersListValidationError")


@_attrs_define
class ApiV1KubernetesClustersListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClustersListCreatedAtErrorComponent |
            ApiV1KubernetesClustersListCreatedByComponentErrorComponent |
            ApiV1KubernetesClustersListCreatedByUsersErrorComponent | ApiV1KubernetesClustersListKindErrorComponent |
            ApiV1KubernetesClustersListKubernetesVersionErrorComponent | ApiV1KubernetesClustersListNameErrorComponent |
            ApiV1KubernetesClustersListNameExactErrorComponent | ApiV1KubernetesClustersListOrganizationsErrorComponent |
            ApiV1KubernetesClustersListScopeErrorComponent | ApiV1KubernetesClustersListSearchErrorComponent |
            ApiV1KubernetesClustersListStateErrorComponent | ApiV1KubernetesClustersListStateNotErrorComponent |
            ApiV1KubernetesClustersListTimeRangeErrorComponent | ApiV1KubernetesClustersListUpdatedAtErrorComponent |
            ApiV1KubernetesClustersListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClustersListCreatedAtErrorComponent
        | ApiV1KubernetesClustersListCreatedByComponentErrorComponent
        | ApiV1KubernetesClustersListCreatedByUsersErrorComponent
        | ApiV1KubernetesClustersListKindErrorComponent
        | ApiV1KubernetesClustersListKubernetesVersionErrorComponent
        | ApiV1KubernetesClustersListNameErrorComponent
        | ApiV1KubernetesClustersListNameExactErrorComponent
        | ApiV1KubernetesClustersListOrganizationsErrorComponent
        | ApiV1KubernetesClustersListScopeErrorComponent
        | ApiV1KubernetesClustersListSearchErrorComponent
        | ApiV1KubernetesClustersListStateErrorComponent
        | ApiV1KubernetesClustersListStateNotErrorComponent
        | ApiV1KubernetesClustersListTimeRangeErrorComponent
        | ApiV1KubernetesClustersListUpdatedAtErrorComponent
        | ApiV1KubernetesClustersListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_clusters_list_created_at_error_component import (
            ApiV1KubernetesClustersListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_created_by_component_error_component import (
            ApiV1KubernetesClustersListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_created_by_users_error_component import (
            ApiV1KubernetesClustersListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_kind_error_component import (
            ApiV1KubernetesClustersListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_kubernetes_version_error_component import (
            ApiV1KubernetesClustersListKubernetesVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_name_error_component import (
            ApiV1KubernetesClustersListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_organizations_error_component import (
            ApiV1KubernetesClustersListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_scope_error_component import (
            ApiV1KubernetesClustersListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_search_error_component import (
            ApiV1KubernetesClustersListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_state_error_component import (
            ApiV1KubernetesClustersListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_state_not_error_component import (
            ApiV1KubernetesClustersListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_time_range_error_component import (
            ApiV1KubernetesClustersListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_updated_at_error_component import (
            ApiV1KubernetesClustersListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_workspaces_error_component import (
            ApiV1KubernetesClustersListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClustersListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListKubernetesVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersListStateNotErrorComponent):
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
        from ..models.api_v1_kubernetes_clusters_list_created_at_error_component import (
            ApiV1KubernetesClustersListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_created_by_component_error_component import (
            ApiV1KubernetesClustersListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_created_by_users_error_component import (
            ApiV1KubernetesClustersListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_kind_error_component import (
            ApiV1KubernetesClustersListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_kubernetes_version_error_component import (
            ApiV1KubernetesClustersListKubernetesVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_name_error_component import (
            ApiV1KubernetesClustersListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_name_exact_error_component import (
            ApiV1KubernetesClustersListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_organizations_error_component import (
            ApiV1KubernetesClustersListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_scope_error_component import (
            ApiV1KubernetesClustersListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_search_error_component import (
            ApiV1KubernetesClustersListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_state_error_component import (
            ApiV1KubernetesClustersListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_state_not_error_component import (
            ApiV1KubernetesClustersListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_time_range_error_component import (
            ApiV1KubernetesClustersListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_updated_at_error_component import (
            ApiV1KubernetesClustersListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_list_workspaces_error_component import (
            ApiV1KubernetesClustersListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClustersListCreatedAtErrorComponent
                | ApiV1KubernetesClustersListCreatedByComponentErrorComponent
                | ApiV1KubernetesClustersListCreatedByUsersErrorComponent
                | ApiV1KubernetesClustersListKindErrorComponent
                | ApiV1KubernetesClustersListKubernetesVersionErrorComponent
                | ApiV1KubernetesClustersListNameErrorComponent
                | ApiV1KubernetesClustersListNameExactErrorComponent
                | ApiV1KubernetesClustersListOrganizationsErrorComponent
                | ApiV1KubernetesClustersListScopeErrorComponent
                | ApiV1KubernetesClustersListSearchErrorComponent
                | ApiV1KubernetesClustersListStateErrorComponent
                | ApiV1KubernetesClustersListStateNotErrorComponent
                | ApiV1KubernetesClustersListTimeRangeErrorComponent
                | ApiV1KubernetesClustersListUpdatedAtErrorComponent
                | ApiV1KubernetesClustersListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_0 = (
                        ApiV1KubernetesClustersListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_1 = (
                        ApiV1KubernetesClustersListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_2 = (
                        ApiV1KubernetesClustersListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_3 = (
                        ApiV1KubernetesClustersListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_4 = (
                        ApiV1KubernetesClustersListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_5 = (
                        ApiV1KubernetesClustersListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_6 = (
                        ApiV1KubernetesClustersListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_7 = (
                        ApiV1KubernetesClustersListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_8 = (
                        ApiV1KubernetesClustersListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_9 = (
                        ApiV1KubernetesClustersListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_10 = (
                        ApiV1KubernetesClustersListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_11 = (
                        ApiV1KubernetesClustersListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_12 = (
                        ApiV1KubernetesClustersListKubernetesVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_list_error_type_13 = (
                        ApiV1KubernetesClustersListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_clusters_list_error_type_14 = (
                    ApiV1KubernetesClustersListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_clusters_list_error_type_14

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_clusters_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_clusters_list_validation_error.additional_properties = d
        return api_v1_kubernetes_clusters_list_validation_error

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
