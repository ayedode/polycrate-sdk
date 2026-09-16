from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_endpoints_list_created_at_error_component import ApiV1EndpointsListCreatedAtErrorComponent
    from ..models.api_v1_endpoints_list_created_by_component_error_component import (
        ApiV1EndpointsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_endpoints_list_created_by_users_error_component import (
        ApiV1EndpointsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_endpoints_list_k8s_app_error_component import ApiV1EndpointsListK8SAppErrorComponent
    from ..models.api_v1_endpoints_list_k8s_cluster_error_component import ApiV1EndpointsListK8SClusterErrorComponent
    from ..models.api_v1_endpoints_list_kind_error_component import ApiV1EndpointsListKindErrorComponent
    from ..models.api_v1_endpoints_list_loadbalancer_instance_error_component import (
        ApiV1EndpointsListLoadbalancerInstanceErrorComponent,
    )
    from ..models.api_v1_endpoints_list_name_error_component import ApiV1EndpointsListNameErrorComponent
    from ..models.api_v1_endpoints_list_name_exact_error_component import ApiV1EndpointsListNameExactErrorComponent
    from ..models.api_v1_endpoints_list_organizations_error_component import (
        ApiV1EndpointsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_endpoints_list_region_error_component import ApiV1EndpointsListRegionErrorComponent
    from ..models.api_v1_endpoints_list_remote_address_error_component import (
        ApiV1EndpointsListRemoteAddressErrorComponent,
    )
    from ..models.api_v1_endpoints_list_remote_port_error_component import ApiV1EndpointsListRemotePortErrorComponent
    from ..models.api_v1_endpoints_list_resolved_ip_error_component import ApiV1EndpointsListResolvedIpErrorComponent
    from ..models.api_v1_endpoints_list_s3_cluster_error_component import ApiV1EndpointsListS3ClusterErrorComponent
    from ..models.api_v1_endpoints_list_scope_error_component import ApiV1EndpointsListScopeErrorComponent
    from ..models.api_v1_endpoints_list_search_error_component import ApiV1EndpointsListSearchErrorComponent
    from ..models.api_v1_endpoints_list_state_error_component import ApiV1EndpointsListStateErrorComponent
    from ..models.api_v1_endpoints_list_state_not_error_component import ApiV1EndpointsListStateNotErrorComponent
    from ..models.api_v1_endpoints_list_time_range_error_component import ApiV1EndpointsListTimeRangeErrorComponent
    from ..models.api_v1_endpoints_list_updated_at_error_component import ApiV1EndpointsListUpdatedAtErrorComponent
    from ..models.api_v1_endpoints_list_workspaces_error_component import ApiV1EndpointsListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1EndpointsListValidationError")


@_attrs_define
class ApiV1EndpointsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1EndpointsListCreatedAtErrorComponent | ApiV1EndpointsListCreatedByComponentErrorComponent |
            ApiV1EndpointsListCreatedByUsersErrorComponent | ApiV1EndpointsListK8SAppErrorComponent |
            ApiV1EndpointsListK8SClusterErrorComponent | ApiV1EndpointsListKindErrorComponent |
            ApiV1EndpointsListLoadbalancerInstanceErrorComponent | ApiV1EndpointsListNameErrorComponent |
            ApiV1EndpointsListNameExactErrorComponent | ApiV1EndpointsListOrganizationsErrorComponent |
            ApiV1EndpointsListRegionErrorComponent | ApiV1EndpointsListRemoteAddressErrorComponent |
            ApiV1EndpointsListRemotePortErrorComponent | ApiV1EndpointsListResolvedIpErrorComponent |
            ApiV1EndpointsListS3ClusterErrorComponent | ApiV1EndpointsListScopeErrorComponent |
            ApiV1EndpointsListSearchErrorComponent | ApiV1EndpointsListStateErrorComponent |
            ApiV1EndpointsListStateNotErrorComponent | ApiV1EndpointsListTimeRangeErrorComponent |
            ApiV1EndpointsListUpdatedAtErrorComponent | ApiV1EndpointsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1EndpointsListCreatedAtErrorComponent
        | ApiV1EndpointsListCreatedByComponentErrorComponent
        | ApiV1EndpointsListCreatedByUsersErrorComponent
        | ApiV1EndpointsListK8SAppErrorComponent
        | ApiV1EndpointsListK8SClusterErrorComponent
        | ApiV1EndpointsListKindErrorComponent
        | ApiV1EndpointsListLoadbalancerInstanceErrorComponent
        | ApiV1EndpointsListNameErrorComponent
        | ApiV1EndpointsListNameExactErrorComponent
        | ApiV1EndpointsListOrganizationsErrorComponent
        | ApiV1EndpointsListRegionErrorComponent
        | ApiV1EndpointsListRemoteAddressErrorComponent
        | ApiV1EndpointsListRemotePortErrorComponent
        | ApiV1EndpointsListResolvedIpErrorComponent
        | ApiV1EndpointsListS3ClusterErrorComponent
        | ApiV1EndpointsListScopeErrorComponent
        | ApiV1EndpointsListSearchErrorComponent
        | ApiV1EndpointsListStateErrorComponent
        | ApiV1EndpointsListStateNotErrorComponent
        | ApiV1EndpointsListTimeRangeErrorComponent
        | ApiV1EndpointsListUpdatedAtErrorComponent
        | ApiV1EndpointsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_endpoints_list_created_at_error_component import (
            ApiV1EndpointsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_created_by_component_error_component import (
            ApiV1EndpointsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_created_by_users_error_component import (
            ApiV1EndpointsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_k8s_app_error_component import (
            ApiV1EndpointsListK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_k8s_cluster_error_component import (
            ApiV1EndpointsListK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_kind_error_component import (
            ApiV1EndpointsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_name_error_component import (
            ApiV1EndpointsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_name_exact_error_component import (
            ApiV1EndpointsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_organizations_error_component import (
            ApiV1EndpointsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_region_error_component import (
            ApiV1EndpointsListRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_remote_address_error_component import (
            ApiV1EndpointsListRemoteAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_remote_port_error_component import (
            ApiV1EndpointsListRemotePortErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_resolved_ip_error_component import (
            ApiV1EndpointsListResolvedIpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_s3_cluster_error_component import (
            ApiV1EndpointsListS3ClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_scope_error_component import (
            ApiV1EndpointsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_search_error_component import (
            ApiV1EndpointsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_state_error_component import (
            ApiV1EndpointsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_state_not_error_component import (
            ApiV1EndpointsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_time_range_error_component import (
            ApiV1EndpointsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_updated_at_error_component import (
            ApiV1EndpointsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_workspaces_error_component import (
            ApiV1EndpointsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1EndpointsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListNameExactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListS3ClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListRemoteAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListRemotePortErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsListResolvedIpErrorComponent):
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
        from ..models.api_v1_endpoints_list_created_at_error_component import (
            ApiV1EndpointsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_created_by_component_error_component import (
            ApiV1EndpointsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_created_by_users_error_component import (
            ApiV1EndpointsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_k8s_app_error_component import (
            ApiV1EndpointsListK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_k8s_cluster_error_component import (
            ApiV1EndpointsListK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_kind_error_component import (
            ApiV1EndpointsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_loadbalancer_instance_error_component import (
            ApiV1EndpointsListLoadbalancerInstanceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_name_error_component import (
            ApiV1EndpointsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_name_exact_error_component import (
            ApiV1EndpointsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_organizations_error_component import (
            ApiV1EndpointsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_region_error_component import (
            ApiV1EndpointsListRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_remote_address_error_component import (
            ApiV1EndpointsListRemoteAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_remote_port_error_component import (
            ApiV1EndpointsListRemotePortErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_resolved_ip_error_component import (
            ApiV1EndpointsListResolvedIpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_s3_cluster_error_component import (
            ApiV1EndpointsListS3ClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_scope_error_component import (
            ApiV1EndpointsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_search_error_component import (
            ApiV1EndpointsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_state_error_component import (
            ApiV1EndpointsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_state_not_error_component import (
            ApiV1EndpointsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_time_range_error_component import (
            ApiV1EndpointsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_updated_at_error_component import (
            ApiV1EndpointsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_list_workspaces_error_component import (
            ApiV1EndpointsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1EndpointsListCreatedAtErrorComponent
                | ApiV1EndpointsListCreatedByComponentErrorComponent
                | ApiV1EndpointsListCreatedByUsersErrorComponent
                | ApiV1EndpointsListK8SAppErrorComponent
                | ApiV1EndpointsListK8SClusterErrorComponent
                | ApiV1EndpointsListKindErrorComponent
                | ApiV1EndpointsListLoadbalancerInstanceErrorComponent
                | ApiV1EndpointsListNameErrorComponent
                | ApiV1EndpointsListNameExactErrorComponent
                | ApiV1EndpointsListOrganizationsErrorComponent
                | ApiV1EndpointsListRegionErrorComponent
                | ApiV1EndpointsListRemoteAddressErrorComponent
                | ApiV1EndpointsListRemotePortErrorComponent
                | ApiV1EndpointsListResolvedIpErrorComponent
                | ApiV1EndpointsListS3ClusterErrorComponent
                | ApiV1EndpointsListScopeErrorComponent
                | ApiV1EndpointsListSearchErrorComponent
                | ApiV1EndpointsListStateErrorComponent
                | ApiV1EndpointsListStateNotErrorComponent
                | ApiV1EndpointsListTimeRangeErrorComponent
                | ApiV1EndpointsListUpdatedAtErrorComponent
                | ApiV1EndpointsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_0 = (
                        ApiV1EndpointsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_1 = (
                        ApiV1EndpointsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_2 = (
                        ApiV1EndpointsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_3 = (
                        ApiV1EndpointsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_4 = (
                        ApiV1EndpointsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_5 = (
                        ApiV1EndpointsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_6 = (
                        ApiV1EndpointsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_7 = (
                        ApiV1EndpointsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_8 = (
                        ApiV1EndpointsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_9 = (
                        ApiV1EndpointsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_10 = (
                        ApiV1EndpointsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_11 = (
                        ApiV1EndpointsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_12 = (
                        ApiV1EndpointsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_13 = (
                        ApiV1EndpointsListNameExactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_14 = (
                        ApiV1EndpointsListK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_15 = (
                        ApiV1EndpointsListK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_16 = (
                        ApiV1EndpointsListS3ClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_17 = (
                        ApiV1EndpointsListRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_18 = (
                        ApiV1EndpointsListRemoteAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_19 = (
                        ApiV1EndpointsListRemotePortErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_list_error_type_20 = (
                        ApiV1EndpointsListResolvedIpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_list_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_endpoints_list_error_type_21 = (
                    ApiV1EndpointsListLoadbalancerInstanceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_endpoints_list_error_type_21

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_endpoints_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_endpoints_list_validation_error.additional_properties = d
        return api_v1_endpoints_list_validation_error

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
