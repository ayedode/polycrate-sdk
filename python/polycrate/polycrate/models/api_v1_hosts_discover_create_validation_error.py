from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_hosts_discover_create_active_error_component import (
        ApiV1HostsDiscoverCreateActiveErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_alias_error_component import ApiV1HostsDiscoverCreateAliasErrorComponent
    from ..models.api_v1_hosts_discover_create_annotations_error_component import (
        ApiV1HostsDiscoverCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_archived_at_error_component import (
        ApiV1HostsDiscoverCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_archived_error_component import (
        ApiV1HostsDiscoverCreateArchivedErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_archived_reason_error_component import (
        ApiV1HostsDiscoverCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_created_by_component_error_component import (
        ApiV1HostsDiscoverCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_credential_error_component import (
        ApiV1HostsDiscoverCreateCredentialErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_criticality_error_component import (
        ApiV1HostsDiscoverCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_debug_mode_error_component import (
        ApiV1HostsDiscoverCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_default_ipv_4_error_component import (
        ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_default_ipv_6_error_component import (
        ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_description_error_component import (
        ApiV1HostsDiscoverCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_display_name_error_component import (
        ApiV1HostsDiscoverCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_hostname_error_component import (
        ApiV1HostsDiscoverCreateHostnameErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_k8s_cluster_error_component import (
        ApiV1HostsDiscoverCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_kind_error_component import ApiV1HostsDiscoverCreateKindErrorComponent
    from ..models.api_v1_hosts_discover_create_labels_error_component import (
        ApiV1HostsDiscoverCreateLabelsErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_name_error_component import ApiV1HostsDiscoverCreateNameErrorComponent
    from ..models.api_v1_hosts_discover_create_non_field_errors_error_component import (
        ApiV1HostsDiscoverCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_platform_service_error_component import (
        ApiV1HostsDiscoverCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_product_id_error_component import (
        ApiV1HostsDiscoverCreateProductIdErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_provider_account_id_error_component import (
        ApiV1HostsDiscoverCreateProviderAccountIdErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_provider_error_component import (
        ApiV1HostsDiscoverCreateProviderErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_provider_image_error_component import (
        ApiV1HostsDiscoverCreateProviderImageErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_provider_image_os_architecture_error_component import (
        ApiV1HostsDiscoverCreateProviderImageOsArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_provider_image_os_flavor_error_component import (
        ApiV1HostsDiscoverCreateProviderImageOsFlavorErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_provider_image_os_version_error_component import (
        ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_provider_location_error_component import (
        ApiV1HostsDiscoverCreateProviderLocationErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_provider_reference_error_component import (
        ApiV1HostsDiscoverCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_provider_type_error_component import (
        ApiV1HostsDiscoverCreateProviderTypeErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_reconciliation_enabled_error_component import (
        ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_resource_cpu_architecture_error_component import (
        ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_resource_cpu_cores_error_component import (
        ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_resource_cpu_type_error_component import (
        ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_resource_disk_error_component import (
        ApiV1HostsDiscoverCreateResourceDiskErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_resource_memory_error_component import (
        ApiV1HostsDiscoverCreateResourceMemoryErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_role_error_component import ApiV1HostsDiscoverCreateRoleErrorComponent
    from ..models.api_v1_hosts_discover_create_sla_availability_error_component import (
        ApiV1HostsDiscoverCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_sla_target_error_component import (
        ApiV1HostsDiscoverCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_slo_availability_error_component import (
        ApiV1HostsDiscoverCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_slo_target_error_component import (
        ApiV1HostsDiscoverCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_ssh_keys_id_error_component import (
        ApiV1HostsDiscoverCreateSshKeysIdErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_target_availability_error_component import (
        ApiV1HostsDiscoverCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_discover_create_tolerations_error_component import (
        ApiV1HostsDiscoverCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1HostsDiscoverCreateValidationError")


@_attrs_define
class ApiV1HostsDiscoverCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1HostsDiscoverCreateActiveErrorComponent | ApiV1HostsDiscoverCreateAliasErrorComponent |
            ApiV1HostsDiscoverCreateAnnotationsErrorComponent | ApiV1HostsDiscoverCreateArchivedAtErrorComponent |
            ApiV1HostsDiscoverCreateArchivedErrorComponent | ApiV1HostsDiscoverCreateArchivedReasonErrorComponent |
            ApiV1HostsDiscoverCreateCreatedByComponentErrorComponent | ApiV1HostsDiscoverCreateCredentialErrorComponent |
            ApiV1HostsDiscoverCreateCriticalityErrorComponent | ApiV1HostsDiscoverCreateDebugModeErrorComponent |
            ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponent | ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponent |
            ApiV1HostsDiscoverCreateDescriptionErrorComponent | ApiV1HostsDiscoverCreateDisplayNameErrorComponent |
            ApiV1HostsDiscoverCreateHostnameErrorComponent | ApiV1HostsDiscoverCreateK8SClusterErrorComponent |
            ApiV1HostsDiscoverCreateKindErrorComponent | ApiV1HostsDiscoverCreateLabelsErrorComponent |
            ApiV1HostsDiscoverCreateNameErrorComponent | ApiV1HostsDiscoverCreateNonFieldErrorsErrorComponent |
            ApiV1HostsDiscoverCreatePlatformServiceErrorComponent | ApiV1HostsDiscoverCreateProductIdErrorComponent |
            ApiV1HostsDiscoverCreateProviderAccountIdErrorComponent | ApiV1HostsDiscoverCreateProviderErrorComponent |
            ApiV1HostsDiscoverCreateProviderImageErrorComponent |
            ApiV1HostsDiscoverCreateProviderImageOsArchitectureErrorComponent |
            ApiV1HostsDiscoverCreateProviderImageOsFlavorErrorComponent |
            ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponent |
            ApiV1HostsDiscoverCreateProviderLocationErrorComponent | ApiV1HostsDiscoverCreateProviderReferenceErrorComponent
            | ApiV1HostsDiscoverCreateProviderTypeErrorComponent |
            ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponent |
            ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponent |
            ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponent | ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponent |
            ApiV1HostsDiscoverCreateResourceDiskErrorComponent | ApiV1HostsDiscoverCreateResourceMemoryErrorComponent |
            ApiV1HostsDiscoverCreateRoleErrorComponent | ApiV1HostsDiscoverCreateSlaAvailabilityErrorComponent |
            ApiV1HostsDiscoverCreateSlaTargetErrorComponent | ApiV1HostsDiscoverCreateSloAvailabilityErrorComponent |
            ApiV1HostsDiscoverCreateSloTargetErrorComponent | ApiV1HostsDiscoverCreateSshKeysIdErrorComponent |
            ApiV1HostsDiscoverCreateTargetAvailabilityErrorComponent | ApiV1HostsDiscoverCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1HostsDiscoverCreateActiveErrorComponent
        | ApiV1HostsDiscoverCreateAliasErrorComponent
        | ApiV1HostsDiscoverCreateAnnotationsErrorComponent
        | ApiV1HostsDiscoverCreateArchivedAtErrorComponent
        | ApiV1HostsDiscoverCreateArchivedErrorComponent
        | ApiV1HostsDiscoverCreateArchivedReasonErrorComponent
        | ApiV1HostsDiscoverCreateCreatedByComponentErrorComponent
        | ApiV1HostsDiscoverCreateCredentialErrorComponent
        | ApiV1HostsDiscoverCreateCriticalityErrorComponent
        | ApiV1HostsDiscoverCreateDebugModeErrorComponent
        | ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponent
        | ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponent
        | ApiV1HostsDiscoverCreateDescriptionErrorComponent
        | ApiV1HostsDiscoverCreateDisplayNameErrorComponent
        | ApiV1HostsDiscoverCreateHostnameErrorComponent
        | ApiV1HostsDiscoverCreateK8SClusterErrorComponent
        | ApiV1HostsDiscoverCreateKindErrorComponent
        | ApiV1HostsDiscoverCreateLabelsErrorComponent
        | ApiV1HostsDiscoverCreateNameErrorComponent
        | ApiV1HostsDiscoverCreateNonFieldErrorsErrorComponent
        | ApiV1HostsDiscoverCreatePlatformServiceErrorComponent
        | ApiV1HostsDiscoverCreateProductIdErrorComponent
        | ApiV1HostsDiscoverCreateProviderAccountIdErrorComponent
        | ApiV1HostsDiscoverCreateProviderErrorComponent
        | ApiV1HostsDiscoverCreateProviderImageErrorComponent
        | ApiV1HostsDiscoverCreateProviderImageOsArchitectureErrorComponent
        | ApiV1HostsDiscoverCreateProviderImageOsFlavorErrorComponent
        | ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponent
        | ApiV1HostsDiscoverCreateProviderLocationErrorComponent
        | ApiV1HostsDiscoverCreateProviderReferenceErrorComponent
        | ApiV1HostsDiscoverCreateProviderTypeErrorComponent
        | ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponent
        | ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponent
        | ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponent
        | ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponent
        | ApiV1HostsDiscoverCreateResourceDiskErrorComponent
        | ApiV1HostsDiscoverCreateResourceMemoryErrorComponent
        | ApiV1HostsDiscoverCreateRoleErrorComponent
        | ApiV1HostsDiscoverCreateSlaAvailabilityErrorComponent
        | ApiV1HostsDiscoverCreateSlaTargetErrorComponent
        | ApiV1HostsDiscoverCreateSloAvailabilityErrorComponent
        | ApiV1HostsDiscoverCreateSloTargetErrorComponent
        | ApiV1HostsDiscoverCreateSshKeysIdErrorComponent
        | ApiV1HostsDiscoverCreateTargetAvailabilityErrorComponent
        | ApiV1HostsDiscoverCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_hosts_discover_create_active_error_component import (
            ApiV1HostsDiscoverCreateActiveErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_alias_error_component import (
            ApiV1HostsDiscoverCreateAliasErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_annotations_error_component import (
            ApiV1HostsDiscoverCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_archived_at_error_component import (
            ApiV1HostsDiscoverCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_archived_error_component import (
            ApiV1HostsDiscoverCreateArchivedErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_archived_reason_error_component import (
            ApiV1HostsDiscoverCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_created_by_component_error_component import (
            ApiV1HostsDiscoverCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_credential_error_component import (
            ApiV1HostsDiscoverCreateCredentialErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_criticality_error_component import (
            ApiV1HostsDiscoverCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_debug_mode_error_component import (
            ApiV1HostsDiscoverCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_default_ipv_4_error_component import (
            ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_default_ipv_6_error_component import (
            ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_description_error_component import (
            ApiV1HostsDiscoverCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_display_name_error_component import (
            ApiV1HostsDiscoverCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_hostname_error_component import (
            ApiV1HostsDiscoverCreateHostnameErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_k8s_cluster_error_component import (
            ApiV1HostsDiscoverCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_kind_error_component import (
            ApiV1HostsDiscoverCreateKindErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_labels_error_component import (
            ApiV1HostsDiscoverCreateLabelsErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_name_error_component import (
            ApiV1HostsDiscoverCreateNameErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_non_field_errors_error_component import (
            ApiV1HostsDiscoverCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_platform_service_error_component import (
            ApiV1HostsDiscoverCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_account_id_error_component import (
            ApiV1HostsDiscoverCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_error_component import (
            ApiV1HostsDiscoverCreateProviderErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_image_error_component import (
            ApiV1HostsDiscoverCreateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_image_os_architecture_error_component import (
            ApiV1HostsDiscoverCreateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_image_os_flavor_error_component import (
            ApiV1HostsDiscoverCreateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_image_os_version_error_component import (
            ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_location_error_component import (
            ApiV1HostsDiscoverCreateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_reference_error_component import (
            ApiV1HostsDiscoverCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_type_error_component import (
            ApiV1HostsDiscoverCreateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_reconciliation_enabled_error_component import (
            ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_resource_cpu_architecture_error_component import (
            ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_resource_cpu_cores_error_component import (
            ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_resource_cpu_type_error_component import (
            ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_resource_disk_error_component import (
            ApiV1HostsDiscoverCreateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_resource_memory_error_component import (
            ApiV1HostsDiscoverCreateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_role_error_component import (
            ApiV1HostsDiscoverCreateRoleErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_sla_availability_error_component import (
            ApiV1HostsDiscoverCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_sla_target_error_component import (
            ApiV1HostsDiscoverCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_slo_availability_error_component import (
            ApiV1HostsDiscoverCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_slo_target_error_component import (
            ApiV1HostsDiscoverCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_ssh_keys_id_error_component import (
            ApiV1HostsDiscoverCreateSshKeysIdErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_target_availability_error_component import (
            ApiV1HostsDiscoverCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_tolerations_error_component import (
            ApiV1HostsDiscoverCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1HostsDiscoverCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateResourceMemoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateResourceDiskErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateProviderLocationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateProviderImageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateProviderImageOsFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateProviderImageOsArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateProviderTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateProviderAccountIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateSshKeysIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsDiscoverCreateK8SClusterErrorComponent):
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
        from ..models.api_v1_hosts_discover_create_active_error_component import (
            ApiV1HostsDiscoverCreateActiveErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_alias_error_component import (
            ApiV1HostsDiscoverCreateAliasErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_annotations_error_component import (
            ApiV1HostsDiscoverCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_archived_at_error_component import (
            ApiV1HostsDiscoverCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_archived_error_component import (
            ApiV1HostsDiscoverCreateArchivedErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_archived_reason_error_component import (
            ApiV1HostsDiscoverCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_created_by_component_error_component import (
            ApiV1HostsDiscoverCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_credential_error_component import (
            ApiV1HostsDiscoverCreateCredentialErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_criticality_error_component import (
            ApiV1HostsDiscoverCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_debug_mode_error_component import (
            ApiV1HostsDiscoverCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_default_ipv_4_error_component import (
            ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_default_ipv_6_error_component import (
            ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_description_error_component import (
            ApiV1HostsDiscoverCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_display_name_error_component import (
            ApiV1HostsDiscoverCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_hostname_error_component import (
            ApiV1HostsDiscoverCreateHostnameErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_k8s_cluster_error_component import (
            ApiV1HostsDiscoverCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_kind_error_component import (
            ApiV1HostsDiscoverCreateKindErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_labels_error_component import (
            ApiV1HostsDiscoverCreateLabelsErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_name_error_component import (
            ApiV1HostsDiscoverCreateNameErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_non_field_errors_error_component import (
            ApiV1HostsDiscoverCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_platform_service_error_component import (
            ApiV1HostsDiscoverCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_product_id_error_component import (
            ApiV1HostsDiscoverCreateProductIdErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_account_id_error_component import (
            ApiV1HostsDiscoverCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_error_component import (
            ApiV1HostsDiscoverCreateProviderErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_image_error_component import (
            ApiV1HostsDiscoverCreateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_image_os_architecture_error_component import (
            ApiV1HostsDiscoverCreateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_image_os_flavor_error_component import (
            ApiV1HostsDiscoverCreateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_image_os_version_error_component import (
            ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_location_error_component import (
            ApiV1HostsDiscoverCreateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_reference_error_component import (
            ApiV1HostsDiscoverCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_provider_type_error_component import (
            ApiV1HostsDiscoverCreateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_reconciliation_enabled_error_component import (
            ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_resource_cpu_architecture_error_component import (
            ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_resource_cpu_cores_error_component import (
            ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_resource_cpu_type_error_component import (
            ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_resource_disk_error_component import (
            ApiV1HostsDiscoverCreateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_resource_memory_error_component import (
            ApiV1HostsDiscoverCreateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_role_error_component import (
            ApiV1HostsDiscoverCreateRoleErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_sla_availability_error_component import (
            ApiV1HostsDiscoverCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_sla_target_error_component import (
            ApiV1HostsDiscoverCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_slo_availability_error_component import (
            ApiV1HostsDiscoverCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_slo_target_error_component import (
            ApiV1HostsDiscoverCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_ssh_keys_id_error_component import (
            ApiV1HostsDiscoverCreateSshKeysIdErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_target_availability_error_component import (
            ApiV1HostsDiscoverCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_discover_create_tolerations_error_component import (
            ApiV1HostsDiscoverCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1HostsDiscoverCreateActiveErrorComponent
                | ApiV1HostsDiscoverCreateAliasErrorComponent
                | ApiV1HostsDiscoverCreateAnnotationsErrorComponent
                | ApiV1HostsDiscoverCreateArchivedAtErrorComponent
                | ApiV1HostsDiscoverCreateArchivedErrorComponent
                | ApiV1HostsDiscoverCreateArchivedReasonErrorComponent
                | ApiV1HostsDiscoverCreateCreatedByComponentErrorComponent
                | ApiV1HostsDiscoverCreateCredentialErrorComponent
                | ApiV1HostsDiscoverCreateCriticalityErrorComponent
                | ApiV1HostsDiscoverCreateDebugModeErrorComponent
                | ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponent
                | ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponent
                | ApiV1HostsDiscoverCreateDescriptionErrorComponent
                | ApiV1HostsDiscoverCreateDisplayNameErrorComponent
                | ApiV1HostsDiscoverCreateHostnameErrorComponent
                | ApiV1HostsDiscoverCreateK8SClusterErrorComponent
                | ApiV1HostsDiscoverCreateKindErrorComponent
                | ApiV1HostsDiscoverCreateLabelsErrorComponent
                | ApiV1HostsDiscoverCreateNameErrorComponent
                | ApiV1HostsDiscoverCreateNonFieldErrorsErrorComponent
                | ApiV1HostsDiscoverCreatePlatformServiceErrorComponent
                | ApiV1HostsDiscoverCreateProductIdErrorComponent
                | ApiV1HostsDiscoverCreateProviderAccountIdErrorComponent
                | ApiV1HostsDiscoverCreateProviderErrorComponent
                | ApiV1HostsDiscoverCreateProviderImageErrorComponent
                | ApiV1HostsDiscoverCreateProviderImageOsArchitectureErrorComponent
                | ApiV1HostsDiscoverCreateProviderImageOsFlavorErrorComponent
                | ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponent
                | ApiV1HostsDiscoverCreateProviderLocationErrorComponent
                | ApiV1HostsDiscoverCreateProviderReferenceErrorComponent
                | ApiV1HostsDiscoverCreateProviderTypeErrorComponent
                | ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponent
                | ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponent
                | ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponent
                | ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponent
                | ApiV1HostsDiscoverCreateResourceDiskErrorComponent
                | ApiV1HostsDiscoverCreateResourceMemoryErrorComponent
                | ApiV1HostsDiscoverCreateRoleErrorComponent
                | ApiV1HostsDiscoverCreateSlaAvailabilityErrorComponent
                | ApiV1HostsDiscoverCreateSlaTargetErrorComponent
                | ApiV1HostsDiscoverCreateSloAvailabilityErrorComponent
                | ApiV1HostsDiscoverCreateSloTargetErrorComponent
                | ApiV1HostsDiscoverCreateSshKeysIdErrorComponent
                | ApiV1HostsDiscoverCreateTargetAvailabilityErrorComponent
                | ApiV1HostsDiscoverCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_0 = (
                        ApiV1HostsDiscoverCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_1 = (
                        ApiV1HostsDiscoverCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_2 = (
                        ApiV1HostsDiscoverCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_3 = (
                        ApiV1HostsDiscoverCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_4 = (
                        ApiV1HostsDiscoverCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_5 = (
                        ApiV1HostsDiscoverCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_6 = (
                        ApiV1HostsDiscoverCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_7 = (
                        ApiV1HostsDiscoverCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_8 = (
                        ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_9 = (
                        ApiV1HostsDiscoverCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_10 = (
                        ApiV1HostsDiscoverCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_11 = (
                        ApiV1HostsDiscoverCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_12 = (
                        ApiV1HostsDiscoverCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_13 = (
                        ApiV1HostsDiscoverCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_14 = (
                        ApiV1HostsDiscoverCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_15 = (
                        ApiV1HostsDiscoverCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_16 = (
                        ApiV1HostsDiscoverCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_17 = (
                        ApiV1HostsDiscoverCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_18 = (
                        ApiV1HostsDiscoverCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_19 = (
                        ApiV1HostsDiscoverCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_20 = (
                        ApiV1HostsDiscoverCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_21 = (
                        ApiV1HostsDiscoverCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_22 = (
                        ApiV1HostsDiscoverCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_23 = (
                        ApiV1HostsDiscoverCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_24 = (
                        ApiV1HostsDiscoverCreateRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_25 = (
                        ApiV1HostsDiscoverCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_26 = (
                        ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_27 = (
                        ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_28 = (
                        ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_29 = (
                        ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_30 = (
                        ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_31 = (
                        ApiV1HostsDiscoverCreateResourceMemoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_32 = (
                        ApiV1HostsDiscoverCreateResourceDiskErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_33 = (
                        ApiV1HostsDiscoverCreateProviderLocationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_34 = (
                        ApiV1HostsDiscoverCreateProviderImageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_35 = (
                        ApiV1HostsDiscoverCreateProviderImageOsFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_36 = (
                        ApiV1HostsDiscoverCreateProviderImageOsVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_37 = (
                        ApiV1HostsDiscoverCreateProviderImageOsArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_38 = (
                        ApiV1HostsDiscoverCreateProviderTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_39 = (
                        ApiV1HostsDiscoverCreateProviderAccountIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_40 = (
                        ApiV1HostsDiscoverCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_41 = (
                        ApiV1HostsDiscoverCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_42 = (
                        ApiV1HostsDiscoverCreateSshKeysIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_discover_create_error_type_43 = (
                        ApiV1HostsDiscoverCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_discover_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_hosts_discover_create_error_type_44 = (
                    ApiV1HostsDiscoverCreateProductIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_hosts_discover_create_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_hosts_discover_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_hosts_discover_create_validation_error.additional_properties = d
        return api_v1_hosts_discover_create_validation_error

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
