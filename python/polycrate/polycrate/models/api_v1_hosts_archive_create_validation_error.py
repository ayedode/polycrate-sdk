from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_hosts_archive_create_active_error_component import ApiV1HostsArchiveCreateActiveErrorComponent
    from ..models.api_v1_hosts_archive_create_alias_error_component import ApiV1HostsArchiveCreateAliasErrorComponent
    from ..models.api_v1_hosts_archive_create_annotations_error_component import (
        ApiV1HostsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_archived_at_error_component import (
        ApiV1HostsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_archived_error_component import (
        ApiV1HostsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_archived_reason_error_component import (
        ApiV1HostsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_created_by_component_error_component import (
        ApiV1HostsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_credential_error_component import (
        ApiV1HostsArchiveCreateCredentialErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_criticality_error_component import (
        ApiV1HostsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_debug_mode_error_component import (
        ApiV1HostsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_default_ipv_4_error_component import (
        ApiV1HostsArchiveCreateDefaultIpv4ErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_default_ipv_6_error_component import (
        ApiV1HostsArchiveCreateDefaultIpv6ErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_description_error_component import (
        ApiV1HostsArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_display_name_error_component import (
        ApiV1HostsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_hostname_error_component import (
        ApiV1HostsArchiveCreateHostnameErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_k8s_cluster_error_component import (
        ApiV1HostsArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_kind_error_component import ApiV1HostsArchiveCreateKindErrorComponent
    from ..models.api_v1_hosts_archive_create_labels_error_component import ApiV1HostsArchiveCreateLabelsErrorComponent
    from ..models.api_v1_hosts_archive_create_name_error_component import ApiV1HostsArchiveCreateNameErrorComponent
    from ..models.api_v1_hosts_archive_create_non_field_errors_error_component import (
        ApiV1HostsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_platform_service_error_component import (
        ApiV1HostsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_product_id_error_component import (
        ApiV1HostsArchiveCreateProductIdErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_provider_account_id_error_component import (
        ApiV1HostsArchiveCreateProviderAccountIdErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_provider_error_component import (
        ApiV1HostsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_provider_image_error_component import (
        ApiV1HostsArchiveCreateProviderImageErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_provider_image_os_architecture_error_component import (
        ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_provider_image_os_flavor_error_component import (
        ApiV1HostsArchiveCreateProviderImageOsFlavorErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_provider_image_os_version_error_component import (
        ApiV1HostsArchiveCreateProviderImageOsVersionErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_provider_location_error_component import (
        ApiV1HostsArchiveCreateProviderLocationErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_provider_reference_error_component import (
        ApiV1HostsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_provider_type_error_component import (
        ApiV1HostsArchiveCreateProviderTypeErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_reconciliation_enabled_error_component import (
        ApiV1HostsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_resource_cpu_architecture_error_component import (
        ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_resource_cpu_cores_error_component import (
        ApiV1HostsArchiveCreateResourceCpuCoresErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_resource_cpu_type_error_component import (
        ApiV1HostsArchiveCreateResourceCpuTypeErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_resource_disk_error_component import (
        ApiV1HostsArchiveCreateResourceDiskErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_resource_memory_error_component import (
        ApiV1HostsArchiveCreateResourceMemoryErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_role_error_component import ApiV1HostsArchiveCreateRoleErrorComponent
    from ..models.api_v1_hosts_archive_create_sla_availability_error_component import (
        ApiV1HostsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_sla_target_error_component import (
        ApiV1HostsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_slo_availability_error_component import (
        ApiV1HostsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_slo_target_error_component import (
        ApiV1HostsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_ssh_keys_id_error_component import (
        ApiV1HostsArchiveCreateSshKeysIdErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_target_availability_error_component import (
        ApiV1HostsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_archive_create_tolerations_error_component import (
        ApiV1HostsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1HostsArchiveCreateValidationError")


@_attrs_define
class ApiV1HostsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1HostsArchiveCreateActiveErrorComponent | ApiV1HostsArchiveCreateAliasErrorComponent |
            ApiV1HostsArchiveCreateAnnotationsErrorComponent | ApiV1HostsArchiveCreateArchivedAtErrorComponent |
            ApiV1HostsArchiveCreateArchivedErrorComponent | ApiV1HostsArchiveCreateArchivedReasonErrorComponent |
            ApiV1HostsArchiveCreateCreatedByComponentErrorComponent | ApiV1HostsArchiveCreateCredentialErrorComponent |
            ApiV1HostsArchiveCreateCriticalityErrorComponent | ApiV1HostsArchiveCreateDebugModeErrorComponent |
            ApiV1HostsArchiveCreateDefaultIpv4ErrorComponent | ApiV1HostsArchiveCreateDefaultIpv6ErrorComponent |
            ApiV1HostsArchiveCreateDescriptionErrorComponent | ApiV1HostsArchiveCreateDisplayNameErrorComponent |
            ApiV1HostsArchiveCreateHostnameErrorComponent | ApiV1HostsArchiveCreateK8SClusterErrorComponent |
            ApiV1HostsArchiveCreateKindErrorComponent | ApiV1HostsArchiveCreateLabelsErrorComponent |
            ApiV1HostsArchiveCreateNameErrorComponent | ApiV1HostsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1HostsArchiveCreatePlatformServiceErrorComponent | ApiV1HostsArchiveCreateProductIdErrorComponent |
            ApiV1HostsArchiveCreateProviderAccountIdErrorComponent | ApiV1HostsArchiveCreateProviderErrorComponent |
            ApiV1HostsArchiveCreateProviderImageErrorComponent |
            ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponent |
            ApiV1HostsArchiveCreateProviderImageOsFlavorErrorComponent |
            ApiV1HostsArchiveCreateProviderImageOsVersionErrorComponent |
            ApiV1HostsArchiveCreateProviderLocationErrorComponent | ApiV1HostsArchiveCreateProviderReferenceErrorComponent |
            ApiV1HostsArchiveCreateProviderTypeErrorComponent | ApiV1HostsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponent |
            ApiV1HostsArchiveCreateResourceCpuCoresErrorComponent | ApiV1HostsArchiveCreateResourceCpuTypeErrorComponent |
            ApiV1HostsArchiveCreateResourceDiskErrorComponent | ApiV1HostsArchiveCreateResourceMemoryErrorComponent |
            ApiV1HostsArchiveCreateRoleErrorComponent | ApiV1HostsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1HostsArchiveCreateSlaTargetErrorComponent | ApiV1HostsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1HostsArchiveCreateSloTargetErrorComponent | ApiV1HostsArchiveCreateSshKeysIdErrorComponent |
            ApiV1HostsArchiveCreateTargetAvailabilityErrorComponent | ApiV1HostsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1HostsArchiveCreateActiveErrorComponent
        | ApiV1HostsArchiveCreateAliasErrorComponent
        | ApiV1HostsArchiveCreateAnnotationsErrorComponent
        | ApiV1HostsArchiveCreateArchivedAtErrorComponent
        | ApiV1HostsArchiveCreateArchivedErrorComponent
        | ApiV1HostsArchiveCreateArchivedReasonErrorComponent
        | ApiV1HostsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1HostsArchiveCreateCredentialErrorComponent
        | ApiV1HostsArchiveCreateCriticalityErrorComponent
        | ApiV1HostsArchiveCreateDebugModeErrorComponent
        | ApiV1HostsArchiveCreateDefaultIpv4ErrorComponent
        | ApiV1HostsArchiveCreateDefaultIpv6ErrorComponent
        | ApiV1HostsArchiveCreateDescriptionErrorComponent
        | ApiV1HostsArchiveCreateDisplayNameErrorComponent
        | ApiV1HostsArchiveCreateHostnameErrorComponent
        | ApiV1HostsArchiveCreateK8SClusterErrorComponent
        | ApiV1HostsArchiveCreateKindErrorComponent
        | ApiV1HostsArchiveCreateLabelsErrorComponent
        | ApiV1HostsArchiveCreateNameErrorComponent
        | ApiV1HostsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1HostsArchiveCreatePlatformServiceErrorComponent
        | ApiV1HostsArchiveCreateProductIdErrorComponent
        | ApiV1HostsArchiveCreateProviderAccountIdErrorComponent
        | ApiV1HostsArchiveCreateProviderErrorComponent
        | ApiV1HostsArchiveCreateProviderImageErrorComponent
        | ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponent
        | ApiV1HostsArchiveCreateProviderImageOsFlavorErrorComponent
        | ApiV1HostsArchiveCreateProviderImageOsVersionErrorComponent
        | ApiV1HostsArchiveCreateProviderLocationErrorComponent
        | ApiV1HostsArchiveCreateProviderReferenceErrorComponent
        | ApiV1HostsArchiveCreateProviderTypeErrorComponent
        | ApiV1HostsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponent
        | ApiV1HostsArchiveCreateResourceCpuCoresErrorComponent
        | ApiV1HostsArchiveCreateResourceCpuTypeErrorComponent
        | ApiV1HostsArchiveCreateResourceDiskErrorComponent
        | ApiV1HostsArchiveCreateResourceMemoryErrorComponent
        | ApiV1HostsArchiveCreateRoleErrorComponent
        | ApiV1HostsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1HostsArchiveCreateSlaTargetErrorComponent
        | ApiV1HostsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1HostsArchiveCreateSloTargetErrorComponent
        | ApiV1HostsArchiveCreateSshKeysIdErrorComponent
        | ApiV1HostsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1HostsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_hosts_archive_create_active_error_component import (
            ApiV1HostsArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_alias_error_component import (
            ApiV1HostsArchiveCreateAliasErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_annotations_error_component import (
            ApiV1HostsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_archived_at_error_component import (
            ApiV1HostsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_archived_error_component import (
            ApiV1HostsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_archived_reason_error_component import (
            ApiV1HostsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_created_by_component_error_component import (
            ApiV1HostsArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_credential_error_component import (
            ApiV1HostsArchiveCreateCredentialErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_criticality_error_component import (
            ApiV1HostsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_debug_mode_error_component import (
            ApiV1HostsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_default_ipv_4_error_component import (
            ApiV1HostsArchiveCreateDefaultIpv4ErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_default_ipv_6_error_component import (
            ApiV1HostsArchiveCreateDefaultIpv6ErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_description_error_component import (
            ApiV1HostsArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_display_name_error_component import (
            ApiV1HostsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_hostname_error_component import (
            ApiV1HostsArchiveCreateHostnameErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_k8s_cluster_error_component import (
            ApiV1HostsArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_kind_error_component import ApiV1HostsArchiveCreateKindErrorComponent
        from ..models.api_v1_hosts_archive_create_labels_error_component import (
            ApiV1HostsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_name_error_component import ApiV1HostsArchiveCreateNameErrorComponent
        from ..models.api_v1_hosts_archive_create_non_field_errors_error_component import (
            ApiV1HostsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_platform_service_error_component import (
            ApiV1HostsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_account_id_error_component import (
            ApiV1HostsArchiveCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_error_component import (
            ApiV1HostsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_image_error_component import (
            ApiV1HostsArchiveCreateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_image_os_architecture_error_component import (
            ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_image_os_flavor_error_component import (
            ApiV1HostsArchiveCreateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_image_os_version_error_component import (
            ApiV1HostsArchiveCreateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_location_error_component import (
            ApiV1HostsArchiveCreateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_reference_error_component import (
            ApiV1HostsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_type_error_component import (
            ApiV1HostsArchiveCreateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_reconciliation_enabled_error_component import (
            ApiV1HostsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_resource_cpu_architecture_error_component import (
            ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_resource_cpu_cores_error_component import (
            ApiV1HostsArchiveCreateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_resource_cpu_type_error_component import (
            ApiV1HostsArchiveCreateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_resource_disk_error_component import (
            ApiV1HostsArchiveCreateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_resource_memory_error_component import (
            ApiV1HostsArchiveCreateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_role_error_component import ApiV1HostsArchiveCreateRoleErrorComponent
        from ..models.api_v1_hosts_archive_create_sla_availability_error_component import (
            ApiV1HostsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_sla_target_error_component import (
            ApiV1HostsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_slo_availability_error_component import (
            ApiV1HostsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_slo_target_error_component import (
            ApiV1HostsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_ssh_keys_id_error_component import (
            ApiV1HostsArchiveCreateSshKeysIdErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_target_availability_error_component import (
            ApiV1HostsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_tolerations_error_component import (
            ApiV1HostsArchiveCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1HostsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateDefaultIpv4ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateDefaultIpv6ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateResourceCpuTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateResourceCpuCoresErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateResourceMemoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateResourceDiskErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateProviderLocationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateProviderImageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateProviderImageOsFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateProviderImageOsVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateProviderTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateProviderAccountIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateSshKeysIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsArchiveCreateK8SClusterErrorComponent):
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
        from ..models.api_v1_hosts_archive_create_active_error_component import (
            ApiV1HostsArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_alias_error_component import (
            ApiV1HostsArchiveCreateAliasErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_annotations_error_component import (
            ApiV1HostsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_archived_at_error_component import (
            ApiV1HostsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_archived_error_component import (
            ApiV1HostsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_archived_reason_error_component import (
            ApiV1HostsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_created_by_component_error_component import (
            ApiV1HostsArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_credential_error_component import (
            ApiV1HostsArchiveCreateCredentialErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_criticality_error_component import (
            ApiV1HostsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_debug_mode_error_component import (
            ApiV1HostsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_default_ipv_4_error_component import (
            ApiV1HostsArchiveCreateDefaultIpv4ErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_default_ipv_6_error_component import (
            ApiV1HostsArchiveCreateDefaultIpv6ErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_description_error_component import (
            ApiV1HostsArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_display_name_error_component import (
            ApiV1HostsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_hostname_error_component import (
            ApiV1HostsArchiveCreateHostnameErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_k8s_cluster_error_component import (
            ApiV1HostsArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_kind_error_component import ApiV1HostsArchiveCreateKindErrorComponent
        from ..models.api_v1_hosts_archive_create_labels_error_component import (
            ApiV1HostsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_name_error_component import ApiV1HostsArchiveCreateNameErrorComponent
        from ..models.api_v1_hosts_archive_create_non_field_errors_error_component import (
            ApiV1HostsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_platform_service_error_component import (
            ApiV1HostsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_product_id_error_component import (
            ApiV1HostsArchiveCreateProductIdErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_account_id_error_component import (
            ApiV1HostsArchiveCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_error_component import (
            ApiV1HostsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_image_error_component import (
            ApiV1HostsArchiveCreateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_image_os_architecture_error_component import (
            ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_image_os_flavor_error_component import (
            ApiV1HostsArchiveCreateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_image_os_version_error_component import (
            ApiV1HostsArchiveCreateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_location_error_component import (
            ApiV1HostsArchiveCreateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_reference_error_component import (
            ApiV1HostsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_provider_type_error_component import (
            ApiV1HostsArchiveCreateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_reconciliation_enabled_error_component import (
            ApiV1HostsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_resource_cpu_architecture_error_component import (
            ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_resource_cpu_cores_error_component import (
            ApiV1HostsArchiveCreateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_resource_cpu_type_error_component import (
            ApiV1HostsArchiveCreateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_resource_disk_error_component import (
            ApiV1HostsArchiveCreateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_resource_memory_error_component import (
            ApiV1HostsArchiveCreateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_role_error_component import ApiV1HostsArchiveCreateRoleErrorComponent
        from ..models.api_v1_hosts_archive_create_sla_availability_error_component import (
            ApiV1HostsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_sla_target_error_component import (
            ApiV1HostsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_slo_availability_error_component import (
            ApiV1HostsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_slo_target_error_component import (
            ApiV1HostsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_ssh_keys_id_error_component import (
            ApiV1HostsArchiveCreateSshKeysIdErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_target_availability_error_component import (
            ApiV1HostsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_archive_create_tolerations_error_component import (
            ApiV1HostsArchiveCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1HostsArchiveCreateActiveErrorComponent
                | ApiV1HostsArchiveCreateAliasErrorComponent
                | ApiV1HostsArchiveCreateAnnotationsErrorComponent
                | ApiV1HostsArchiveCreateArchivedAtErrorComponent
                | ApiV1HostsArchiveCreateArchivedErrorComponent
                | ApiV1HostsArchiveCreateArchivedReasonErrorComponent
                | ApiV1HostsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1HostsArchiveCreateCredentialErrorComponent
                | ApiV1HostsArchiveCreateCriticalityErrorComponent
                | ApiV1HostsArchiveCreateDebugModeErrorComponent
                | ApiV1HostsArchiveCreateDefaultIpv4ErrorComponent
                | ApiV1HostsArchiveCreateDefaultIpv6ErrorComponent
                | ApiV1HostsArchiveCreateDescriptionErrorComponent
                | ApiV1HostsArchiveCreateDisplayNameErrorComponent
                | ApiV1HostsArchiveCreateHostnameErrorComponent
                | ApiV1HostsArchiveCreateK8SClusterErrorComponent
                | ApiV1HostsArchiveCreateKindErrorComponent
                | ApiV1HostsArchiveCreateLabelsErrorComponent
                | ApiV1HostsArchiveCreateNameErrorComponent
                | ApiV1HostsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1HostsArchiveCreatePlatformServiceErrorComponent
                | ApiV1HostsArchiveCreateProductIdErrorComponent
                | ApiV1HostsArchiveCreateProviderAccountIdErrorComponent
                | ApiV1HostsArchiveCreateProviderErrorComponent
                | ApiV1HostsArchiveCreateProviderImageErrorComponent
                | ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponent
                | ApiV1HostsArchiveCreateProviderImageOsFlavorErrorComponent
                | ApiV1HostsArchiveCreateProviderImageOsVersionErrorComponent
                | ApiV1HostsArchiveCreateProviderLocationErrorComponent
                | ApiV1HostsArchiveCreateProviderReferenceErrorComponent
                | ApiV1HostsArchiveCreateProviderTypeErrorComponent
                | ApiV1HostsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponent
                | ApiV1HostsArchiveCreateResourceCpuCoresErrorComponent
                | ApiV1HostsArchiveCreateResourceCpuTypeErrorComponent
                | ApiV1HostsArchiveCreateResourceDiskErrorComponent
                | ApiV1HostsArchiveCreateResourceMemoryErrorComponent
                | ApiV1HostsArchiveCreateRoleErrorComponent
                | ApiV1HostsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1HostsArchiveCreateSlaTargetErrorComponent
                | ApiV1HostsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1HostsArchiveCreateSloTargetErrorComponent
                | ApiV1HostsArchiveCreateSshKeysIdErrorComponent
                | ApiV1HostsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1HostsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_0 = (
                        ApiV1HostsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_1 = (
                        ApiV1HostsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_2 = (
                        ApiV1HostsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_3 = (
                        ApiV1HostsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_4 = (
                        ApiV1HostsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_5 = (
                        ApiV1HostsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_6 = (
                        ApiV1HostsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_7 = (
                        ApiV1HostsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_8 = (
                        ApiV1HostsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_9 = (
                        ApiV1HostsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_10 = (
                        ApiV1HostsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_11 = (
                        ApiV1HostsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_12 = (
                        ApiV1HostsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_13 = (
                        ApiV1HostsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_14 = (
                        ApiV1HostsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_15 = (
                        ApiV1HostsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_16 = (
                        ApiV1HostsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_17 = (
                        ApiV1HostsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_18 = (
                        ApiV1HostsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_19 = (
                        ApiV1HostsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_20 = (
                        ApiV1HostsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_21 = (
                        ApiV1HostsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_22 = (
                        ApiV1HostsArchiveCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_23 = (
                        ApiV1HostsArchiveCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_24 = (
                        ApiV1HostsArchiveCreateRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_25 = (
                        ApiV1HostsArchiveCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_26 = (
                        ApiV1HostsArchiveCreateDefaultIpv4ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_27 = (
                        ApiV1HostsArchiveCreateDefaultIpv6ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_28 = (
                        ApiV1HostsArchiveCreateResourceCpuTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_29 = (
                        ApiV1HostsArchiveCreateResourceCpuCoresErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_30 = (
                        ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_31 = (
                        ApiV1HostsArchiveCreateResourceMemoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_32 = (
                        ApiV1HostsArchiveCreateResourceDiskErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_33 = (
                        ApiV1HostsArchiveCreateProviderLocationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_34 = (
                        ApiV1HostsArchiveCreateProviderImageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_35 = (
                        ApiV1HostsArchiveCreateProviderImageOsFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_36 = (
                        ApiV1HostsArchiveCreateProviderImageOsVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_37 = (
                        ApiV1HostsArchiveCreateProviderImageOsArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_38 = (
                        ApiV1HostsArchiveCreateProviderTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_39 = (
                        ApiV1HostsArchiveCreateProviderAccountIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_40 = (
                        ApiV1HostsArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_41 = (
                        ApiV1HostsArchiveCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_42 = (
                        ApiV1HostsArchiveCreateSshKeysIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_archive_create_error_type_43 = (
                        ApiV1HostsArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_hosts_archive_create_error_type_44 = (
                    ApiV1HostsArchiveCreateProductIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_hosts_archive_create_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_hosts_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_hosts_archive_create_validation_error.additional_properties = d
        return api_v1_hosts_archive_create_validation_error

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
