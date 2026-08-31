from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_hosts_create_active_error_component import ApiV1HostsCreateActiveErrorComponent
    from ..models.api_v1_hosts_create_alias_error_component import ApiV1HostsCreateAliasErrorComponent
    from ..models.api_v1_hosts_create_annotations_error_component import ApiV1HostsCreateAnnotationsErrorComponent
    from ..models.api_v1_hosts_create_archived_at_error_component import ApiV1HostsCreateArchivedAtErrorComponent
    from ..models.api_v1_hosts_create_archived_error_component import ApiV1HostsCreateArchivedErrorComponent
    from ..models.api_v1_hosts_create_archived_reason_error_component import (
        ApiV1HostsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_hosts_create_created_by_component_error_component import (
        ApiV1HostsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_hosts_create_credential_error_component import ApiV1HostsCreateCredentialErrorComponent
    from ..models.api_v1_hosts_create_criticality_error_component import ApiV1HostsCreateCriticalityErrorComponent
    from ..models.api_v1_hosts_create_debug_mode_error_component import ApiV1HostsCreateDebugModeErrorComponent
    from ..models.api_v1_hosts_create_default_ipv_4_error_component import ApiV1HostsCreateDefaultIpv4ErrorComponent
    from ..models.api_v1_hosts_create_default_ipv_6_error_component import ApiV1HostsCreateDefaultIpv6ErrorComponent
    from ..models.api_v1_hosts_create_description_error_component import ApiV1HostsCreateDescriptionErrorComponent
    from ..models.api_v1_hosts_create_display_name_error_component import ApiV1HostsCreateDisplayNameErrorComponent
    from ..models.api_v1_hosts_create_hostname_error_component import ApiV1HostsCreateHostnameErrorComponent
    from ..models.api_v1_hosts_create_k8s_cluster_error_component import ApiV1HostsCreateK8SClusterErrorComponent
    from ..models.api_v1_hosts_create_kind_error_component import ApiV1HostsCreateKindErrorComponent
    from ..models.api_v1_hosts_create_labels_error_component import ApiV1HostsCreateLabelsErrorComponent
    from ..models.api_v1_hosts_create_name_error_component import ApiV1HostsCreateNameErrorComponent
    from ..models.api_v1_hosts_create_non_field_errors_error_component import (
        ApiV1HostsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_hosts_create_platform_service_error_component import (
        ApiV1HostsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_hosts_create_product_id_error_component import ApiV1HostsCreateProductIdErrorComponent
    from ..models.api_v1_hosts_create_provider_account_id_error_component import (
        ApiV1HostsCreateProviderAccountIdErrorComponent,
    )
    from ..models.api_v1_hosts_create_provider_error_component import ApiV1HostsCreateProviderErrorComponent
    from ..models.api_v1_hosts_create_provider_image_error_component import ApiV1HostsCreateProviderImageErrorComponent
    from ..models.api_v1_hosts_create_provider_image_os_architecture_error_component import (
        ApiV1HostsCreateProviderImageOsArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_create_provider_image_os_flavor_error_component import (
        ApiV1HostsCreateProviderImageOsFlavorErrorComponent,
    )
    from ..models.api_v1_hosts_create_provider_image_os_version_error_component import (
        ApiV1HostsCreateProviderImageOsVersionErrorComponent,
    )
    from ..models.api_v1_hosts_create_provider_location_error_component import (
        ApiV1HostsCreateProviderLocationErrorComponent,
    )
    from ..models.api_v1_hosts_create_provider_reference_error_component import (
        ApiV1HostsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_hosts_create_provider_type_error_component import ApiV1HostsCreateProviderTypeErrorComponent
    from ..models.api_v1_hosts_create_reconciliation_enabled_error_component import (
        ApiV1HostsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_hosts_create_resource_cpu_architecture_error_component import (
        ApiV1HostsCreateResourceCpuArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_create_resource_cpu_cores_error_component import (
        ApiV1HostsCreateResourceCpuCoresErrorComponent,
    )
    from ..models.api_v1_hosts_create_resource_cpu_type_error_component import (
        ApiV1HostsCreateResourceCpuTypeErrorComponent,
    )
    from ..models.api_v1_hosts_create_resource_disk_error_component import ApiV1HostsCreateResourceDiskErrorComponent
    from ..models.api_v1_hosts_create_resource_memory_error_component import (
        ApiV1HostsCreateResourceMemoryErrorComponent,
    )
    from ..models.api_v1_hosts_create_role_error_component import ApiV1HostsCreateRoleErrorComponent
    from ..models.api_v1_hosts_create_sla_availability_error_component import (
        ApiV1HostsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_create_sla_target_error_component import ApiV1HostsCreateSlaTargetErrorComponent
    from ..models.api_v1_hosts_create_slo_availability_error_component import (
        ApiV1HostsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_create_slo_target_error_component import ApiV1HostsCreateSloTargetErrorComponent
    from ..models.api_v1_hosts_create_ssh_keys_id_error_component import ApiV1HostsCreateSshKeysIdErrorComponent
    from ..models.api_v1_hosts_create_target_availability_error_component import (
        ApiV1HostsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_create_tolerations_error_component import ApiV1HostsCreateTolerationsErrorComponent


T = TypeVar("T", bound="ApiV1HostsCreateValidationError")


@_attrs_define
class ApiV1HostsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1HostsCreateActiveErrorComponent | ApiV1HostsCreateAliasErrorComponent |
            ApiV1HostsCreateAnnotationsErrorComponent | ApiV1HostsCreateArchivedAtErrorComponent |
            ApiV1HostsCreateArchivedErrorComponent | ApiV1HostsCreateArchivedReasonErrorComponent |
            ApiV1HostsCreateCreatedByComponentErrorComponent | ApiV1HostsCreateCredentialErrorComponent |
            ApiV1HostsCreateCriticalityErrorComponent | ApiV1HostsCreateDebugModeErrorComponent |
            ApiV1HostsCreateDefaultIpv4ErrorComponent | ApiV1HostsCreateDefaultIpv6ErrorComponent |
            ApiV1HostsCreateDescriptionErrorComponent | ApiV1HostsCreateDisplayNameErrorComponent |
            ApiV1HostsCreateHostnameErrorComponent | ApiV1HostsCreateK8SClusterErrorComponent |
            ApiV1HostsCreateKindErrorComponent | ApiV1HostsCreateLabelsErrorComponent | ApiV1HostsCreateNameErrorComponent |
            ApiV1HostsCreateNonFieldErrorsErrorComponent | ApiV1HostsCreatePlatformServiceErrorComponent |
            ApiV1HostsCreateProductIdErrorComponent | ApiV1HostsCreateProviderAccountIdErrorComponent |
            ApiV1HostsCreateProviderErrorComponent | ApiV1HostsCreateProviderImageErrorComponent |
            ApiV1HostsCreateProviderImageOsArchitectureErrorComponent | ApiV1HostsCreateProviderImageOsFlavorErrorComponent
            | ApiV1HostsCreateProviderImageOsVersionErrorComponent | ApiV1HostsCreateProviderLocationErrorComponent |
            ApiV1HostsCreateProviderReferenceErrorComponent | ApiV1HostsCreateProviderTypeErrorComponent |
            ApiV1HostsCreateReconciliationEnabledErrorComponent | ApiV1HostsCreateResourceCpuArchitectureErrorComponent |
            ApiV1HostsCreateResourceCpuCoresErrorComponent | ApiV1HostsCreateResourceCpuTypeErrorComponent |
            ApiV1HostsCreateResourceDiskErrorComponent | ApiV1HostsCreateResourceMemoryErrorComponent |
            ApiV1HostsCreateRoleErrorComponent | ApiV1HostsCreateSlaAvailabilityErrorComponent |
            ApiV1HostsCreateSlaTargetErrorComponent | ApiV1HostsCreateSloAvailabilityErrorComponent |
            ApiV1HostsCreateSloTargetErrorComponent | ApiV1HostsCreateSshKeysIdErrorComponent |
            ApiV1HostsCreateTargetAvailabilityErrorComponent | ApiV1HostsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1HostsCreateActiveErrorComponent
        | ApiV1HostsCreateAliasErrorComponent
        | ApiV1HostsCreateAnnotationsErrorComponent
        | ApiV1HostsCreateArchivedAtErrorComponent
        | ApiV1HostsCreateArchivedErrorComponent
        | ApiV1HostsCreateArchivedReasonErrorComponent
        | ApiV1HostsCreateCreatedByComponentErrorComponent
        | ApiV1HostsCreateCredentialErrorComponent
        | ApiV1HostsCreateCriticalityErrorComponent
        | ApiV1HostsCreateDebugModeErrorComponent
        | ApiV1HostsCreateDefaultIpv4ErrorComponent
        | ApiV1HostsCreateDefaultIpv6ErrorComponent
        | ApiV1HostsCreateDescriptionErrorComponent
        | ApiV1HostsCreateDisplayNameErrorComponent
        | ApiV1HostsCreateHostnameErrorComponent
        | ApiV1HostsCreateK8SClusterErrorComponent
        | ApiV1HostsCreateKindErrorComponent
        | ApiV1HostsCreateLabelsErrorComponent
        | ApiV1HostsCreateNameErrorComponent
        | ApiV1HostsCreateNonFieldErrorsErrorComponent
        | ApiV1HostsCreatePlatformServiceErrorComponent
        | ApiV1HostsCreateProductIdErrorComponent
        | ApiV1HostsCreateProviderAccountIdErrorComponent
        | ApiV1HostsCreateProviderErrorComponent
        | ApiV1HostsCreateProviderImageErrorComponent
        | ApiV1HostsCreateProviderImageOsArchitectureErrorComponent
        | ApiV1HostsCreateProviderImageOsFlavorErrorComponent
        | ApiV1HostsCreateProviderImageOsVersionErrorComponent
        | ApiV1HostsCreateProviderLocationErrorComponent
        | ApiV1HostsCreateProviderReferenceErrorComponent
        | ApiV1HostsCreateProviderTypeErrorComponent
        | ApiV1HostsCreateReconciliationEnabledErrorComponent
        | ApiV1HostsCreateResourceCpuArchitectureErrorComponent
        | ApiV1HostsCreateResourceCpuCoresErrorComponent
        | ApiV1HostsCreateResourceCpuTypeErrorComponent
        | ApiV1HostsCreateResourceDiskErrorComponent
        | ApiV1HostsCreateResourceMemoryErrorComponent
        | ApiV1HostsCreateRoleErrorComponent
        | ApiV1HostsCreateSlaAvailabilityErrorComponent
        | ApiV1HostsCreateSlaTargetErrorComponent
        | ApiV1HostsCreateSloAvailabilityErrorComponent
        | ApiV1HostsCreateSloTargetErrorComponent
        | ApiV1HostsCreateSshKeysIdErrorComponent
        | ApiV1HostsCreateTargetAvailabilityErrorComponent
        | ApiV1HostsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_hosts_create_active_error_component import ApiV1HostsCreateActiveErrorComponent
        from ..models.api_v1_hosts_create_alias_error_component import ApiV1HostsCreateAliasErrorComponent
        from ..models.api_v1_hosts_create_annotations_error_component import ApiV1HostsCreateAnnotationsErrorComponent
        from ..models.api_v1_hosts_create_archived_at_error_component import ApiV1HostsCreateArchivedAtErrorComponent
        from ..models.api_v1_hosts_create_archived_error_component import ApiV1HostsCreateArchivedErrorComponent
        from ..models.api_v1_hosts_create_archived_reason_error_component import (
            ApiV1HostsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_create_created_by_component_error_component import (
            ApiV1HostsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_create_credential_error_component import ApiV1HostsCreateCredentialErrorComponent
        from ..models.api_v1_hosts_create_criticality_error_component import ApiV1HostsCreateCriticalityErrorComponent
        from ..models.api_v1_hosts_create_debug_mode_error_component import ApiV1HostsCreateDebugModeErrorComponent
        from ..models.api_v1_hosts_create_default_ipv_4_error_component import ApiV1HostsCreateDefaultIpv4ErrorComponent
        from ..models.api_v1_hosts_create_default_ipv_6_error_component import ApiV1HostsCreateDefaultIpv6ErrorComponent
        from ..models.api_v1_hosts_create_description_error_component import ApiV1HostsCreateDescriptionErrorComponent
        from ..models.api_v1_hosts_create_display_name_error_component import ApiV1HostsCreateDisplayNameErrorComponent
        from ..models.api_v1_hosts_create_hostname_error_component import ApiV1HostsCreateHostnameErrorComponent
        from ..models.api_v1_hosts_create_k8s_cluster_error_component import ApiV1HostsCreateK8SClusterErrorComponent
        from ..models.api_v1_hosts_create_kind_error_component import ApiV1HostsCreateKindErrorComponent
        from ..models.api_v1_hosts_create_labels_error_component import ApiV1HostsCreateLabelsErrorComponent
        from ..models.api_v1_hosts_create_name_error_component import ApiV1HostsCreateNameErrorComponent
        from ..models.api_v1_hosts_create_non_field_errors_error_component import (
            ApiV1HostsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_create_platform_service_error_component import (
            ApiV1HostsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_account_id_error_component import (
            ApiV1HostsCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_error_component import ApiV1HostsCreateProviderErrorComponent
        from ..models.api_v1_hosts_create_provider_image_error_component import (
            ApiV1HostsCreateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_image_os_architecture_error_component import (
            ApiV1HostsCreateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_image_os_flavor_error_component import (
            ApiV1HostsCreateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_image_os_version_error_component import (
            ApiV1HostsCreateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_location_error_component import (
            ApiV1HostsCreateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_reference_error_component import (
            ApiV1HostsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_type_error_component import (
            ApiV1HostsCreateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_create_reconciliation_enabled_error_component import (
            ApiV1HostsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_create_resource_cpu_architecture_error_component import (
            ApiV1HostsCreateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_create_resource_cpu_cores_error_component import (
            ApiV1HostsCreateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_create_resource_cpu_type_error_component import (
            ApiV1HostsCreateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_create_resource_disk_error_component import (
            ApiV1HostsCreateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_create_resource_memory_error_component import (
            ApiV1HostsCreateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_create_role_error_component import ApiV1HostsCreateRoleErrorComponent
        from ..models.api_v1_hosts_create_sla_availability_error_component import (
            ApiV1HostsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_create_sla_target_error_component import ApiV1HostsCreateSlaTargetErrorComponent
        from ..models.api_v1_hosts_create_slo_availability_error_component import (
            ApiV1HostsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_create_slo_target_error_component import ApiV1HostsCreateSloTargetErrorComponent
        from ..models.api_v1_hosts_create_ssh_keys_id_error_component import ApiV1HostsCreateSshKeysIdErrorComponent
        from ..models.api_v1_hosts_create_target_availability_error_component import (
            ApiV1HostsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_create_tolerations_error_component import ApiV1HostsCreateTolerationsErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1HostsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateDefaultIpv4ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateDefaultIpv6ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateResourceCpuTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateResourceCpuCoresErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateResourceCpuArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateResourceMemoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateResourceDiskErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateProviderLocationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateProviderImageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateProviderImageOsFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateProviderImageOsVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateProviderImageOsArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateProviderTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateProviderAccountIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateSshKeysIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsCreateK8SClusterErrorComponent):
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
        from ..models.api_v1_hosts_create_active_error_component import ApiV1HostsCreateActiveErrorComponent
        from ..models.api_v1_hosts_create_alias_error_component import ApiV1HostsCreateAliasErrorComponent
        from ..models.api_v1_hosts_create_annotations_error_component import ApiV1HostsCreateAnnotationsErrorComponent
        from ..models.api_v1_hosts_create_archived_at_error_component import ApiV1HostsCreateArchivedAtErrorComponent
        from ..models.api_v1_hosts_create_archived_error_component import ApiV1HostsCreateArchivedErrorComponent
        from ..models.api_v1_hosts_create_archived_reason_error_component import (
            ApiV1HostsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_create_created_by_component_error_component import (
            ApiV1HostsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_create_credential_error_component import ApiV1HostsCreateCredentialErrorComponent
        from ..models.api_v1_hosts_create_criticality_error_component import ApiV1HostsCreateCriticalityErrorComponent
        from ..models.api_v1_hosts_create_debug_mode_error_component import ApiV1HostsCreateDebugModeErrorComponent
        from ..models.api_v1_hosts_create_default_ipv_4_error_component import ApiV1HostsCreateDefaultIpv4ErrorComponent
        from ..models.api_v1_hosts_create_default_ipv_6_error_component import ApiV1HostsCreateDefaultIpv6ErrorComponent
        from ..models.api_v1_hosts_create_description_error_component import ApiV1HostsCreateDescriptionErrorComponent
        from ..models.api_v1_hosts_create_display_name_error_component import ApiV1HostsCreateDisplayNameErrorComponent
        from ..models.api_v1_hosts_create_hostname_error_component import ApiV1HostsCreateHostnameErrorComponent
        from ..models.api_v1_hosts_create_k8s_cluster_error_component import ApiV1HostsCreateK8SClusterErrorComponent
        from ..models.api_v1_hosts_create_kind_error_component import ApiV1HostsCreateKindErrorComponent
        from ..models.api_v1_hosts_create_labels_error_component import ApiV1HostsCreateLabelsErrorComponent
        from ..models.api_v1_hosts_create_name_error_component import ApiV1HostsCreateNameErrorComponent
        from ..models.api_v1_hosts_create_non_field_errors_error_component import (
            ApiV1HostsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_create_platform_service_error_component import (
            ApiV1HostsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_create_product_id_error_component import ApiV1HostsCreateProductIdErrorComponent
        from ..models.api_v1_hosts_create_provider_account_id_error_component import (
            ApiV1HostsCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_error_component import ApiV1HostsCreateProviderErrorComponent
        from ..models.api_v1_hosts_create_provider_image_error_component import (
            ApiV1HostsCreateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_image_os_architecture_error_component import (
            ApiV1HostsCreateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_image_os_flavor_error_component import (
            ApiV1HostsCreateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_image_os_version_error_component import (
            ApiV1HostsCreateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_location_error_component import (
            ApiV1HostsCreateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_reference_error_component import (
            ApiV1HostsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_create_provider_type_error_component import (
            ApiV1HostsCreateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_create_reconciliation_enabled_error_component import (
            ApiV1HostsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_create_resource_cpu_architecture_error_component import (
            ApiV1HostsCreateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_create_resource_cpu_cores_error_component import (
            ApiV1HostsCreateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_create_resource_cpu_type_error_component import (
            ApiV1HostsCreateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_create_resource_disk_error_component import (
            ApiV1HostsCreateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_create_resource_memory_error_component import (
            ApiV1HostsCreateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_create_role_error_component import ApiV1HostsCreateRoleErrorComponent
        from ..models.api_v1_hosts_create_sla_availability_error_component import (
            ApiV1HostsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_create_sla_target_error_component import ApiV1HostsCreateSlaTargetErrorComponent
        from ..models.api_v1_hosts_create_slo_availability_error_component import (
            ApiV1HostsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_create_slo_target_error_component import ApiV1HostsCreateSloTargetErrorComponent
        from ..models.api_v1_hosts_create_ssh_keys_id_error_component import ApiV1HostsCreateSshKeysIdErrorComponent
        from ..models.api_v1_hosts_create_target_availability_error_component import (
            ApiV1HostsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_create_tolerations_error_component import ApiV1HostsCreateTolerationsErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1HostsCreateActiveErrorComponent
                | ApiV1HostsCreateAliasErrorComponent
                | ApiV1HostsCreateAnnotationsErrorComponent
                | ApiV1HostsCreateArchivedAtErrorComponent
                | ApiV1HostsCreateArchivedErrorComponent
                | ApiV1HostsCreateArchivedReasonErrorComponent
                | ApiV1HostsCreateCreatedByComponentErrorComponent
                | ApiV1HostsCreateCredentialErrorComponent
                | ApiV1HostsCreateCriticalityErrorComponent
                | ApiV1HostsCreateDebugModeErrorComponent
                | ApiV1HostsCreateDefaultIpv4ErrorComponent
                | ApiV1HostsCreateDefaultIpv6ErrorComponent
                | ApiV1HostsCreateDescriptionErrorComponent
                | ApiV1HostsCreateDisplayNameErrorComponent
                | ApiV1HostsCreateHostnameErrorComponent
                | ApiV1HostsCreateK8SClusterErrorComponent
                | ApiV1HostsCreateKindErrorComponent
                | ApiV1HostsCreateLabelsErrorComponent
                | ApiV1HostsCreateNameErrorComponent
                | ApiV1HostsCreateNonFieldErrorsErrorComponent
                | ApiV1HostsCreatePlatformServiceErrorComponent
                | ApiV1HostsCreateProductIdErrorComponent
                | ApiV1HostsCreateProviderAccountIdErrorComponent
                | ApiV1HostsCreateProviderErrorComponent
                | ApiV1HostsCreateProviderImageErrorComponent
                | ApiV1HostsCreateProviderImageOsArchitectureErrorComponent
                | ApiV1HostsCreateProviderImageOsFlavorErrorComponent
                | ApiV1HostsCreateProviderImageOsVersionErrorComponent
                | ApiV1HostsCreateProviderLocationErrorComponent
                | ApiV1HostsCreateProviderReferenceErrorComponent
                | ApiV1HostsCreateProviderTypeErrorComponent
                | ApiV1HostsCreateReconciliationEnabledErrorComponent
                | ApiV1HostsCreateResourceCpuArchitectureErrorComponent
                | ApiV1HostsCreateResourceCpuCoresErrorComponent
                | ApiV1HostsCreateResourceCpuTypeErrorComponent
                | ApiV1HostsCreateResourceDiskErrorComponent
                | ApiV1HostsCreateResourceMemoryErrorComponent
                | ApiV1HostsCreateRoleErrorComponent
                | ApiV1HostsCreateSlaAvailabilityErrorComponent
                | ApiV1HostsCreateSlaTargetErrorComponent
                | ApiV1HostsCreateSloAvailabilityErrorComponent
                | ApiV1HostsCreateSloTargetErrorComponent
                | ApiV1HostsCreateSshKeysIdErrorComponent
                | ApiV1HostsCreateTargetAvailabilityErrorComponent
                | ApiV1HostsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_0 = (
                        ApiV1HostsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_1 = ApiV1HostsCreateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_2 = (
                        ApiV1HostsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_3 = ApiV1HostsCreateLabelsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_4 = (
                        ApiV1HostsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_5 = (
                        ApiV1HostsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_6 = (
                        ApiV1HostsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_7 = (
                        ApiV1HostsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_8 = (
                        ApiV1HostsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_9 = (
                        ApiV1HostsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_10 = ApiV1HostsCreateKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_11 = (
                        ApiV1HostsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_12 = (
                        ApiV1HostsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_13 = (
                        ApiV1HostsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_14 = (
                        ApiV1HostsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_15 = (
                        ApiV1HostsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_16 = (
                        ApiV1HostsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_17 = (
                        ApiV1HostsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_18 = (
                        ApiV1HostsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_19 = (
                        ApiV1HostsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_20 = (
                        ApiV1HostsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_21 = (
                        ApiV1HostsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_22 = (
                        ApiV1HostsCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_23 = ApiV1HostsCreateAliasErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_24 = ApiV1HostsCreateRoleErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_25 = (
                        ApiV1HostsCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_26 = (
                        ApiV1HostsCreateDefaultIpv4ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_27 = (
                        ApiV1HostsCreateDefaultIpv6ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_28 = (
                        ApiV1HostsCreateResourceCpuTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_29 = (
                        ApiV1HostsCreateResourceCpuCoresErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_30 = (
                        ApiV1HostsCreateResourceCpuArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_31 = (
                        ApiV1HostsCreateResourceMemoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_32 = (
                        ApiV1HostsCreateResourceDiskErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_33 = (
                        ApiV1HostsCreateProviderLocationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_34 = (
                        ApiV1HostsCreateProviderImageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_35 = (
                        ApiV1HostsCreateProviderImageOsFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_36 = (
                        ApiV1HostsCreateProviderImageOsVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_37 = (
                        ApiV1HostsCreateProviderImageOsArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_38 = (
                        ApiV1HostsCreateProviderTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_39 = (
                        ApiV1HostsCreateProviderAccountIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_40 = (
                        ApiV1HostsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_41 = (
                        ApiV1HostsCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_42 = (
                        ApiV1HostsCreateSshKeysIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_create_error_type_43 = (
                        ApiV1HostsCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_hosts_create_error_type_44 = ApiV1HostsCreateProductIdErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_hosts_create_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_hosts_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_hosts_create_validation_error.additional_properties = d
        return api_v1_hosts_create_validation_error

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
