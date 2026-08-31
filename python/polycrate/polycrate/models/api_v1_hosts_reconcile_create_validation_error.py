from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_hosts_reconcile_create_active_error_component import (
        ApiV1HostsReconcileCreateActiveErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_alias_error_component import (
        ApiV1HostsReconcileCreateAliasErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_annotations_error_component import (
        ApiV1HostsReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_archived_at_error_component import (
        ApiV1HostsReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_archived_error_component import (
        ApiV1HostsReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_archived_reason_error_component import (
        ApiV1HostsReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_created_by_component_error_component import (
        ApiV1HostsReconcileCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_credential_error_component import (
        ApiV1HostsReconcileCreateCredentialErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_criticality_error_component import (
        ApiV1HostsReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_debug_mode_error_component import (
        ApiV1HostsReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_default_ipv_4_error_component import (
        ApiV1HostsReconcileCreateDefaultIpv4ErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_default_ipv_6_error_component import (
        ApiV1HostsReconcileCreateDefaultIpv6ErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_description_error_component import (
        ApiV1HostsReconcileCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_display_name_error_component import (
        ApiV1HostsReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_hostname_error_component import (
        ApiV1HostsReconcileCreateHostnameErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_k8s_cluster_error_component import (
        ApiV1HostsReconcileCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_kind_error_component import ApiV1HostsReconcileCreateKindErrorComponent
    from ..models.api_v1_hosts_reconcile_create_labels_error_component import (
        ApiV1HostsReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_name_error_component import ApiV1HostsReconcileCreateNameErrorComponent
    from ..models.api_v1_hosts_reconcile_create_non_field_errors_error_component import (
        ApiV1HostsReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_platform_service_error_component import (
        ApiV1HostsReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_product_id_error_component import (
        ApiV1HostsReconcileCreateProductIdErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_provider_account_id_error_component import (
        ApiV1HostsReconcileCreateProviderAccountIdErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_provider_error_component import (
        ApiV1HostsReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_provider_image_error_component import (
        ApiV1HostsReconcileCreateProviderImageErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_provider_image_os_architecture_error_component import (
        ApiV1HostsReconcileCreateProviderImageOsArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_provider_image_os_flavor_error_component import (
        ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_provider_image_os_version_error_component import (
        ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_provider_location_error_component import (
        ApiV1HostsReconcileCreateProviderLocationErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_provider_reference_error_component import (
        ApiV1HostsReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_provider_type_error_component import (
        ApiV1HostsReconcileCreateProviderTypeErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1HostsReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_resource_cpu_architecture_error_component import (
        ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_resource_cpu_cores_error_component import (
        ApiV1HostsReconcileCreateResourceCpuCoresErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_resource_cpu_type_error_component import (
        ApiV1HostsReconcileCreateResourceCpuTypeErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_resource_disk_error_component import (
        ApiV1HostsReconcileCreateResourceDiskErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_resource_memory_error_component import (
        ApiV1HostsReconcileCreateResourceMemoryErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_role_error_component import ApiV1HostsReconcileCreateRoleErrorComponent
    from ..models.api_v1_hosts_reconcile_create_sla_availability_error_component import (
        ApiV1HostsReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_sla_target_error_component import (
        ApiV1HostsReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_slo_availability_error_component import (
        ApiV1HostsReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_slo_target_error_component import (
        ApiV1HostsReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_ssh_keys_id_error_component import (
        ApiV1HostsReconcileCreateSshKeysIdErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_target_availability_error_component import (
        ApiV1HostsReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_reconcile_create_tolerations_error_component import (
        ApiV1HostsReconcileCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1HostsReconcileCreateValidationError")


@_attrs_define
class ApiV1HostsReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1HostsReconcileCreateActiveErrorComponent | ApiV1HostsReconcileCreateAliasErrorComponent |
            ApiV1HostsReconcileCreateAnnotationsErrorComponent | ApiV1HostsReconcileCreateArchivedAtErrorComponent |
            ApiV1HostsReconcileCreateArchivedErrorComponent | ApiV1HostsReconcileCreateArchivedReasonErrorComponent |
            ApiV1HostsReconcileCreateCreatedByComponentErrorComponent | ApiV1HostsReconcileCreateCredentialErrorComponent |
            ApiV1HostsReconcileCreateCriticalityErrorComponent | ApiV1HostsReconcileCreateDebugModeErrorComponent |
            ApiV1HostsReconcileCreateDefaultIpv4ErrorComponent | ApiV1HostsReconcileCreateDefaultIpv6ErrorComponent |
            ApiV1HostsReconcileCreateDescriptionErrorComponent | ApiV1HostsReconcileCreateDisplayNameErrorComponent |
            ApiV1HostsReconcileCreateHostnameErrorComponent | ApiV1HostsReconcileCreateK8SClusterErrorComponent |
            ApiV1HostsReconcileCreateKindErrorComponent | ApiV1HostsReconcileCreateLabelsErrorComponent |
            ApiV1HostsReconcileCreateNameErrorComponent | ApiV1HostsReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1HostsReconcileCreatePlatformServiceErrorComponent | ApiV1HostsReconcileCreateProductIdErrorComponent |
            ApiV1HostsReconcileCreateProviderAccountIdErrorComponent | ApiV1HostsReconcileCreateProviderErrorComponent |
            ApiV1HostsReconcileCreateProviderImageErrorComponent |
            ApiV1HostsReconcileCreateProviderImageOsArchitectureErrorComponent |
            ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponent |
            ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponent |
            ApiV1HostsReconcileCreateProviderLocationErrorComponent |
            ApiV1HostsReconcileCreateProviderReferenceErrorComponent | ApiV1HostsReconcileCreateProviderTypeErrorComponent |
            ApiV1HostsReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponent |
            ApiV1HostsReconcileCreateResourceCpuCoresErrorComponent | ApiV1HostsReconcileCreateResourceCpuTypeErrorComponent
            | ApiV1HostsReconcileCreateResourceDiskErrorComponent | ApiV1HostsReconcileCreateResourceMemoryErrorComponent |
            ApiV1HostsReconcileCreateRoleErrorComponent | ApiV1HostsReconcileCreateSlaAvailabilityErrorComponent |
            ApiV1HostsReconcileCreateSlaTargetErrorComponent | ApiV1HostsReconcileCreateSloAvailabilityErrorComponent |
            ApiV1HostsReconcileCreateSloTargetErrorComponent | ApiV1HostsReconcileCreateSshKeysIdErrorComponent |
            ApiV1HostsReconcileCreateTargetAvailabilityErrorComponent |
            ApiV1HostsReconcileCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1HostsReconcileCreateActiveErrorComponent
        | ApiV1HostsReconcileCreateAliasErrorComponent
        | ApiV1HostsReconcileCreateAnnotationsErrorComponent
        | ApiV1HostsReconcileCreateArchivedAtErrorComponent
        | ApiV1HostsReconcileCreateArchivedErrorComponent
        | ApiV1HostsReconcileCreateArchivedReasonErrorComponent
        | ApiV1HostsReconcileCreateCreatedByComponentErrorComponent
        | ApiV1HostsReconcileCreateCredentialErrorComponent
        | ApiV1HostsReconcileCreateCriticalityErrorComponent
        | ApiV1HostsReconcileCreateDebugModeErrorComponent
        | ApiV1HostsReconcileCreateDefaultIpv4ErrorComponent
        | ApiV1HostsReconcileCreateDefaultIpv6ErrorComponent
        | ApiV1HostsReconcileCreateDescriptionErrorComponent
        | ApiV1HostsReconcileCreateDisplayNameErrorComponent
        | ApiV1HostsReconcileCreateHostnameErrorComponent
        | ApiV1HostsReconcileCreateK8SClusterErrorComponent
        | ApiV1HostsReconcileCreateKindErrorComponent
        | ApiV1HostsReconcileCreateLabelsErrorComponent
        | ApiV1HostsReconcileCreateNameErrorComponent
        | ApiV1HostsReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1HostsReconcileCreatePlatformServiceErrorComponent
        | ApiV1HostsReconcileCreateProductIdErrorComponent
        | ApiV1HostsReconcileCreateProviderAccountIdErrorComponent
        | ApiV1HostsReconcileCreateProviderErrorComponent
        | ApiV1HostsReconcileCreateProviderImageErrorComponent
        | ApiV1HostsReconcileCreateProviderImageOsArchitectureErrorComponent
        | ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponent
        | ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponent
        | ApiV1HostsReconcileCreateProviderLocationErrorComponent
        | ApiV1HostsReconcileCreateProviderReferenceErrorComponent
        | ApiV1HostsReconcileCreateProviderTypeErrorComponent
        | ApiV1HostsReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponent
        | ApiV1HostsReconcileCreateResourceCpuCoresErrorComponent
        | ApiV1HostsReconcileCreateResourceCpuTypeErrorComponent
        | ApiV1HostsReconcileCreateResourceDiskErrorComponent
        | ApiV1HostsReconcileCreateResourceMemoryErrorComponent
        | ApiV1HostsReconcileCreateRoleErrorComponent
        | ApiV1HostsReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1HostsReconcileCreateSlaTargetErrorComponent
        | ApiV1HostsReconcileCreateSloAvailabilityErrorComponent
        | ApiV1HostsReconcileCreateSloTargetErrorComponent
        | ApiV1HostsReconcileCreateSshKeysIdErrorComponent
        | ApiV1HostsReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1HostsReconcileCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_hosts_reconcile_create_active_error_component import (
            ApiV1HostsReconcileCreateActiveErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_alias_error_component import (
            ApiV1HostsReconcileCreateAliasErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_annotations_error_component import (
            ApiV1HostsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_archived_at_error_component import (
            ApiV1HostsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_archived_error_component import (
            ApiV1HostsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_archived_reason_error_component import (
            ApiV1HostsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_created_by_component_error_component import (
            ApiV1HostsReconcileCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_credential_error_component import (
            ApiV1HostsReconcileCreateCredentialErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_criticality_error_component import (
            ApiV1HostsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_debug_mode_error_component import (
            ApiV1HostsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_default_ipv_4_error_component import (
            ApiV1HostsReconcileCreateDefaultIpv4ErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_default_ipv_6_error_component import (
            ApiV1HostsReconcileCreateDefaultIpv6ErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_description_error_component import (
            ApiV1HostsReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_display_name_error_component import (
            ApiV1HostsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_hostname_error_component import (
            ApiV1HostsReconcileCreateHostnameErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_k8s_cluster_error_component import (
            ApiV1HostsReconcileCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_kind_error_component import (
            ApiV1HostsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_labels_error_component import (
            ApiV1HostsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_name_error_component import (
            ApiV1HostsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_non_field_errors_error_component import (
            ApiV1HostsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_platform_service_error_component import (
            ApiV1HostsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_account_id_error_component import (
            ApiV1HostsReconcileCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_error_component import (
            ApiV1HostsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_image_error_component import (
            ApiV1HostsReconcileCreateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_image_os_architecture_error_component import (
            ApiV1HostsReconcileCreateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_image_os_flavor_error_component import (
            ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_image_os_version_error_component import (
            ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_location_error_component import (
            ApiV1HostsReconcileCreateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_reference_error_component import (
            ApiV1HostsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_type_error_component import (
            ApiV1HostsReconcileCreateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1HostsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_resource_cpu_architecture_error_component import (
            ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_resource_cpu_cores_error_component import (
            ApiV1HostsReconcileCreateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_resource_cpu_type_error_component import (
            ApiV1HostsReconcileCreateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_resource_disk_error_component import (
            ApiV1HostsReconcileCreateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_resource_memory_error_component import (
            ApiV1HostsReconcileCreateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_role_error_component import (
            ApiV1HostsReconcileCreateRoleErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_sla_availability_error_component import (
            ApiV1HostsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_sla_target_error_component import (
            ApiV1HostsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_slo_availability_error_component import (
            ApiV1HostsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_slo_target_error_component import (
            ApiV1HostsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_ssh_keys_id_error_component import (
            ApiV1HostsReconcileCreateSshKeysIdErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_target_availability_error_component import (
            ApiV1HostsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_tolerations_error_component import (
            ApiV1HostsReconcileCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1HostsReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateDefaultIpv4ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateDefaultIpv6ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateResourceCpuTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateResourceCpuCoresErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateResourceMemoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateResourceDiskErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateProviderLocationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateProviderImageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateProviderImageOsArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateProviderTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateProviderAccountIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateSshKeysIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsReconcileCreateK8SClusterErrorComponent):
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
        from ..models.api_v1_hosts_reconcile_create_active_error_component import (
            ApiV1HostsReconcileCreateActiveErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_alias_error_component import (
            ApiV1HostsReconcileCreateAliasErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_annotations_error_component import (
            ApiV1HostsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_archived_at_error_component import (
            ApiV1HostsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_archived_error_component import (
            ApiV1HostsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_archived_reason_error_component import (
            ApiV1HostsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_created_by_component_error_component import (
            ApiV1HostsReconcileCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_credential_error_component import (
            ApiV1HostsReconcileCreateCredentialErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_criticality_error_component import (
            ApiV1HostsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_debug_mode_error_component import (
            ApiV1HostsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_default_ipv_4_error_component import (
            ApiV1HostsReconcileCreateDefaultIpv4ErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_default_ipv_6_error_component import (
            ApiV1HostsReconcileCreateDefaultIpv6ErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_description_error_component import (
            ApiV1HostsReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_display_name_error_component import (
            ApiV1HostsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_hostname_error_component import (
            ApiV1HostsReconcileCreateHostnameErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_k8s_cluster_error_component import (
            ApiV1HostsReconcileCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_kind_error_component import (
            ApiV1HostsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_labels_error_component import (
            ApiV1HostsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_name_error_component import (
            ApiV1HostsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_non_field_errors_error_component import (
            ApiV1HostsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_platform_service_error_component import (
            ApiV1HostsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_product_id_error_component import (
            ApiV1HostsReconcileCreateProductIdErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_account_id_error_component import (
            ApiV1HostsReconcileCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_error_component import (
            ApiV1HostsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_image_error_component import (
            ApiV1HostsReconcileCreateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_image_os_architecture_error_component import (
            ApiV1HostsReconcileCreateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_image_os_flavor_error_component import (
            ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_image_os_version_error_component import (
            ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_location_error_component import (
            ApiV1HostsReconcileCreateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_reference_error_component import (
            ApiV1HostsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_provider_type_error_component import (
            ApiV1HostsReconcileCreateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1HostsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_resource_cpu_architecture_error_component import (
            ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_resource_cpu_cores_error_component import (
            ApiV1HostsReconcileCreateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_resource_cpu_type_error_component import (
            ApiV1HostsReconcileCreateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_resource_disk_error_component import (
            ApiV1HostsReconcileCreateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_resource_memory_error_component import (
            ApiV1HostsReconcileCreateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_role_error_component import (
            ApiV1HostsReconcileCreateRoleErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_sla_availability_error_component import (
            ApiV1HostsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_sla_target_error_component import (
            ApiV1HostsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_slo_availability_error_component import (
            ApiV1HostsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_slo_target_error_component import (
            ApiV1HostsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_ssh_keys_id_error_component import (
            ApiV1HostsReconcileCreateSshKeysIdErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_target_availability_error_component import (
            ApiV1HostsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_reconcile_create_tolerations_error_component import (
            ApiV1HostsReconcileCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1HostsReconcileCreateActiveErrorComponent
                | ApiV1HostsReconcileCreateAliasErrorComponent
                | ApiV1HostsReconcileCreateAnnotationsErrorComponent
                | ApiV1HostsReconcileCreateArchivedAtErrorComponent
                | ApiV1HostsReconcileCreateArchivedErrorComponent
                | ApiV1HostsReconcileCreateArchivedReasonErrorComponent
                | ApiV1HostsReconcileCreateCreatedByComponentErrorComponent
                | ApiV1HostsReconcileCreateCredentialErrorComponent
                | ApiV1HostsReconcileCreateCriticalityErrorComponent
                | ApiV1HostsReconcileCreateDebugModeErrorComponent
                | ApiV1HostsReconcileCreateDefaultIpv4ErrorComponent
                | ApiV1HostsReconcileCreateDefaultIpv6ErrorComponent
                | ApiV1HostsReconcileCreateDescriptionErrorComponent
                | ApiV1HostsReconcileCreateDisplayNameErrorComponent
                | ApiV1HostsReconcileCreateHostnameErrorComponent
                | ApiV1HostsReconcileCreateK8SClusterErrorComponent
                | ApiV1HostsReconcileCreateKindErrorComponent
                | ApiV1HostsReconcileCreateLabelsErrorComponent
                | ApiV1HostsReconcileCreateNameErrorComponent
                | ApiV1HostsReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1HostsReconcileCreatePlatformServiceErrorComponent
                | ApiV1HostsReconcileCreateProductIdErrorComponent
                | ApiV1HostsReconcileCreateProviderAccountIdErrorComponent
                | ApiV1HostsReconcileCreateProviderErrorComponent
                | ApiV1HostsReconcileCreateProviderImageErrorComponent
                | ApiV1HostsReconcileCreateProviderImageOsArchitectureErrorComponent
                | ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponent
                | ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponent
                | ApiV1HostsReconcileCreateProviderLocationErrorComponent
                | ApiV1HostsReconcileCreateProviderReferenceErrorComponent
                | ApiV1HostsReconcileCreateProviderTypeErrorComponent
                | ApiV1HostsReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponent
                | ApiV1HostsReconcileCreateResourceCpuCoresErrorComponent
                | ApiV1HostsReconcileCreateResourceCpuTypeErrorComponent
                | ApiV1HostsReconcileCreateResourceDiskErrorComponent
                | ApiV1HostsReconcileCreateResourceMemoryErrorComponent
                | ApiV1HostsReconcileCreateRoleErrorComponent
                | ApiV1HostsReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1HostsReconcileCreateSlaTargetErrorComponent
                | ApiV1HostsReconcileCreateSloAvailabilityErrorComponent
                | ApiV1HostsReconcileCreateSloTargetErrorComponent
                | ApiV1HostsReconcileCreateSshKeysIdErrorComponent
                | ApiV1HostsReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1HostsReconcileCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_0 = (
                        ApiV1HostsReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_1 = (
                        ApiV1HostsReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_2 = (
                        ApiV1HostsReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_3 = (
                        ApiV1HostsReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_4 = (
                        ApiV1HostsReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_5 = (
                        ApiV1HostsReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_6 = (
                        ApiV1HostsReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_7 = (
                        ApiV1HostsReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_8 = (
                        ApiV1HostsReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_9 = (
                        ApiV1HostsReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_10 = (
                        ApiV1HostsReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_11 = (
                        ApiV1HostsReconcileCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_12 = (
                        ApiV1HostsReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_13 = (
                        ApiV1HostsReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_14 = (
                        ApiV1HostsReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_15 = (
                        ApiV1HostsReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_16 = (
                        ApiV1HostsReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_17 = (
                        ApiV1HostsReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_18 = (
                        ApiV1HostsReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_19 = (
                        ApiV1HostsReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_20 = (
                        ApiV1HostsReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_21 = (
                        ApiV1HostsReconcileCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_22 = (
                        ApiV1HostsReconcileCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_23 = (
                        ApiV1HostsReconcileCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_24 = (
                        ApiV1HostsReconcileCreateRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_25 = (
                        ApiV1HostsReconcileCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_26 = (
                        ApiV1HostsReconcileCreateDefaultIpv4ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_27 = (
                        ApiV1HostsReconcileCreateDefaultIpv6ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_28 = (
                        ApiV1HostsReconcileCreateResourceCpuTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_29 = (
                        ApiV1HostsReconcileCreateResourceCpuCoresErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_30 = (
                        ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_31 = (
                        ApiV1HostsReconcileCreateResourceMemoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_32 = (
                        ApiV1HostsReconcileCreateResourceDiskErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_33 = (
                        ApiV1HostsReconcileCreateProviderLocationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_34 = (
                        ApiV1HostsReconcileCreateProviderImageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_35 = (
                        ApiV1HostsReconcileCreateProviderImageOsFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_36 = (
                        ApiV1HostsReconcileCreateProviderImageOsVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_37 = (
                        ApiV1HostsReconcileCreateProviderImageOsArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_38 = (
                        ApiV1HostsReconcileCreateProviderTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_39 = (
                        ApiV1HostsReconcileCreateProviderAccountIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_40 = (
                        ApiV1HostsReconcileCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_41 = (
                        ApiV1HostsReconcileCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_42 = (
                        ApiV1HostsReconcileCreateSshKeysIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_reconcile_create_error_type_43 = (
                        ApiV1HostsReconcileCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_reconcile_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_hosts_reconcile_create_error_type_44 = (
                    ApiV1HostsReconcileCreateProductIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_hosts_reconcile_create_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_hosts_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_hosts_reconcile_create_validation_error.additional_properties = d
        return api_v1_hosts_reconcile_create_validation_error

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
