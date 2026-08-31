from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_hosts_update_active_error_component import ApiV1HostsUpdateActiveErrorComponent
    from ..models.api_v1_hosts_update_alias_error_component import ApiV1HostsUpdateAliasErrorComponent
    from ..models.api_v1_hosts_update_annotations_error_component import ApiV1HostsUpdateAnnotationsErrorComponent
    from ..models.api_v1_hosts_update_archived_at_error_component import ApiV1HostsUpdateArchivedAtErrorComponent
    from ..models.api_v1_hosts_update_archived_error_component import ApiV1HostsUpdateArchivedErrorComponent
    from ..models.api_v1_hosts_update_archived_reason_error_component import (
        ApiV1HostsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_hosts_update_created_by_component_error_component import (
        ApiV1HostsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_hosts_update_credential_error_component import ApiV1HostsUpdateCredentialErrorComponent
    from ..models.api_v1_hosts_update_criticality_error_component import ApiV1HostsUpdateCriticalityErrorComponent
    from ..models.api_v1_hosts_update_debug_mode_error_component import ApiV1HostsUpdateDebugModeErrorComponent
    from ..models.api_v1_hosts_update_default_ipv_4_error_component import ApiV1HostsUpdateDefaultIpv4ErrorComponent
    from ..models.api_v1_hosts_update_default_ipv_6_error_component import ApiV1HostsUpdateDefaultIpv6ErrorComponent
    from ..models.api_v1_hosts_update_description_error_component import ApiV1HostsUpdateDescriptionErrorComponent
    from ..models.api_v1_hosts_update_display_name_error_component import ApiV1HostsUpdateDisplayNameErrorComponent
    from ..models.api_v1_hosts_update_hostname_error_component import ApiV1HostsUpdateHostnameErrorComponent
    from ..models.api_v1_hosts_update_k8s_cluster_error_component import ApiV1HostsUpdateK8SClusterErrorComponent
    from ..models.api_v1_hosts_update_kind_error_component import ApiV1HostsUpdateKindErrorComponent
    from ..models.api_v1_hosts_update_labels_error_component import ApiV1HostsUpdateLabelsErrorComponent
    from ..models.api_v1_hosts_update_name_error_component import ApiV1HostsUpdateNameErrorComponent
    from ..models.api_v1_hosts_update_non_field_errors_error_component import (
        ApiV1HostsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_hosts_update_platform_service_error_component import (
        ApiV1HostsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_hosts_update_product_id_error_component import ApiV1HostsUpdateProductIdErrorComponent
    from ..models.api_v1_hosts_update_provider_account_id_error_component import (
        ApiV1HostsUpdateProviderAccountIdErrorComponent,
    )
    from ..models.api_v1_hosts_update_provider_error_component import ApiV1HostsUpdateProviderErrorComponent
    from ..models.api_v1_hosts_update_provider_image_error_component import ApiV1HostsUpdateProviderImageErrorComponent
    from ..models.api_v1_hosts_update_provider_image_os_architecture_error_component import (
        ApiV1HostsUpdateProviderImageOsArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_update_provider_image_os_flavor_error_component import (
        ApiV1HostsUpdateProviderImageOsFlavorErrorComponent,
    )
    from ..models.api_v1_hosts_update_provider_image_os_version_error_component import (
        ApiV1HostsUpdateProviderImageOsVersionErrorComponent,
    )
    from ..models.api_v1_hosts_update_provider_location_error_component import (
        ApiV1HostsUpdateProviderLocationErrorComponent,
    )
    from ..models.api_v1_hosts_update_provider_reference_error_component import (
        ApiV1HostsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_hosts_update_provider_type_error_component import ApiV1HostsUpdateProviderTypeErrorComponent
    from ..models.api_v1_hosts_update_reconciliation_enabled_error_component import (
        ApiV1HostsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_hosts_update_resource_cpu_architecture_error_component import (
        ApiV1HostsUpdateResourceCpuArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_update_resource_cpu_cores_error_component import (
        ApiV1HostsUpdateResourceCpuCoresErrorComponent,
    )
    from ..models.api_v1_hosts_update_resource_cpu_type_error_component import (
        ApiV1HostsUpdateResourceCpuTypeErrorComponent,
    )
    from ..models.api_v1_hosts_update_resource_disk_error_component import ApiV1HostsUpdateResourceDiskErrorComponent
    from ..models.api_v1_hosts_update_resource_memory_error_component import (
        ApiV1HostsUpdateResourceMemoryErrorComponent,
    )
    from ..models.api_v1_hosts_update_role_error_component import ApiV1HostsUpdateRoleErrorComponent
    from ..models.api_v1_hosts_update_sla_availability_error_component import (
        ApiV1HostsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_update_sla_target_error_component import ApiV1HostsUpdateSlaTargetErrorComponent
    from ..models.api_v1_hosts_update_slo_availability_error_component import (
        ApiV1HostsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_update_slo_target_error_component import ApiV1HostsUpdateSloTargetErrorComponent
    from ..models.api_v1_hosts_update_ssh_keys_id_error_component import ApiV1HostsUpdateSshKeysIdErrorComponent
    from ..models.api_v1_hosts_update_target_availability_error_component import (
        ApiV1HostsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_update_tolerations_error_component import ApiV1HostsUpdateTolerationsErrorComponent


T = TypeVar("T", bound="ApiV1HostsUpdateValidationError")


@_attrs_define
class ApiV1HostsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1HostsUpdateActiveErrorComponent | ApiV1HostsUpdateAliasErrorComponent |
            ApiV1HostsUpdateAnnotationsErrorComponent | ApiV1HostsUpdateArchivedAtErrorComponent |
            ApiV1HostsUpdateArchivedErrorComponent | ApiV1HostsUpdateArchivedReasonErrorComponent |
            ApiV1HostsUpdateCreatedByComponentErrorComponent | ApiV1HostsUpdateCredentialErrorComponent |
            ApiV1HostsUpdateCriticalityErrorComponent | ApiV1HostsUpdateDebugModeErrorComponent |
            ApiV1HostsUpdateDefaultIpv4ErrorComponent | ApiV1HostsUpdateDefaultIpv6ErrorComponent |
            ApiV1HostsUpdateDescriptionErrorComponent | ApiV1HostsUpdateDisplayNameErrorComponent |
            ApiV1HostsUpdateHostnameErrorComponent | ApiV1HostsUpdateK8SClusterErrorComponent |
            ApiV1HostsUpdateKindErrorComponent | ApiV1HostsUpdateLabelsErrorComponent | ApiV1HostsUpdateNameErrorComponent |
            ApiV1HostsUpdateNonFieldErrorsErrorComponent | ApiV1HostsUpdatePlatformServiceErrorComponent |
            ApiV1HostsUpdateProductIdErrorComponent | ApiV1HostsUpdateProviderAccountIdErrorComponent |
            ApiV1HostsUpdateProviderErrorComponent | ApiV1HostsUpdateProviderImageErrorComponent |
            ApiV1HostsUpdateProviderImageOsArchitectureErrorComponent | ApiV1HostsUpdateProviderImageOsFlavorErrorComponent
            | ApiV1HostsUpdateProviderImageOsVersionErrorComponent | ApiV1HostsUpdateProviderLocationErrorComponent |
            ApiV1HostsUpdateProviderReferenceErrorComponent | ApiV1HostsUpdateProviderTypeErrorComponent |
            ApiV1HostsUpdateReconciliationEnabledErrorComponent | ApiV1HostsUpdateResourceCpuArchitectureErrorComponent |
            ApiV1HostsUpdateResourceCpuCoresErrorComponent | ApiV1HostsUpdateResourceCpuTypeErrorComponent |
            ApiV1HostsUpdateResourceDiskErrorComponent | ApiV1HostsUpdateResourceMemoryErrorComponent |
            ApiV1HostsUpdateRoleErrorComponent | ApiV1HostsUpdateSlaAvailabilityErrorComponent |
            ApiV1HostsUpdateSlaTargetErrorComponent | ApiV1HostsUpdateSloAvailabilityErrorComponent |
            ApiV1HostsUpdateSloTargetErrorComponent | ApiV1HostsUpdateSshKeysIdErrorComponent |
            ApiV1HostsUpdateTargetAvailabilityErrorComponent | ApiV1HostsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1HostsUpdateActiveErrorComponent
        | ApiV1HostsUpdateAliasErrorComponent
        | ApiV1HostsUpdateAnnotationsErrorComponent
        | ApiV1HostsUpdateArchivedAtErrorComponent
        | ApiV1HostsUpdateArchivedErrorComponent
        | ApiV1HostsUpdateArchivedReasonErrorComponent
        | ApiV1HostsUpdateCreatedByComponentErrorComponent
        | ApiV1HostsUpdateCredentialErrorComponent
        | ApiV1HostsUpdateCriticalityErrorComponent
        | ApiV1HostsUpdateDebugModeErrorComponent
        | ApiV1HostsUpdateDefaultIpv4ErrorComponent
        | ApiV1HostsUpdateDefaultIpv6ErrorComponent
        | ApiV1HostsUpdateDescriptionErrorComponent
        | ApiV1HostsUpdateDisplayNameErrorComponent
        | ApiV1HostsUpdateHostnameErrorComponent
        | ApiV1HostsUpdateK8SClusterErrorComponent
        | ApiV1HostsUpdateKindErrorComponent
        | ApiV1HostsUpdateLabelsErrorComponent
        | ApiV1HostsUpdateNameErrorComponent
        | ApiV1HostsUpdateNonFieldErrorsErrorComponent
        | ApiV1HostsUpdatePlatformServiceErrorComponent
        | ApiV1HostsUpdateProductIdErrorComponent
        | ApiV1HostsUpdateProviderAccountIdErrorComponent
        | ApiV1HostsUpdateProviderErrorComponent
        | ApiV1HostsUpdateProviderImageErrorComponent
        | ApiV1HostsUpdateProviderImageOsArchitectureErrorComponent
        | ApiV1HostsUpdateProviderImageOsFlavorErrorComponent
        | ApiV1HostsUpdateProviderImageOsVersionErrorComponent
        | ApiV1HostsUpdateProviderLocationErrorComponent
        | ApiV1HostsUpdateProviderReferenceErrorComponent
        | ApiV1HostsUpdateProviderTypeErrorComponent
        | ApiV1HostsUpdateReconciliationEnabledErrorComponent
        | ApiV1HostsUpdateResourceCpuArchitectureErrorComponent
        | ApiV1HostsUpdateResourceCpuCoresErrorComponent
        | ApiV1HostsUpdateResourceCpuTypeErrorComponent
        | ApiV1HostsUpdateResourceDiskErrorComponent
        | ApiV1HostsUpdateResourceMemoryErrorComponent
        | ApiV1HostsUpdateRoleErrorComponent
        | ApiV1HostsUpdateSlaAvailabilityErrorComponent
        | ApiV1HostsUpdateSlaTargetErrorComponent
        | ApiV1HostsUpdateSloAvailabilityErrorComponent
        | ApiV1HostsUpdateSloTargetErrorComponent
        | ApiV1HostsUpdateSshKeysIdErrorComponent
        | ApiV1HostsUpdateTargetAvailabilityErrorComponent
        | ApiV1HostsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_hosts_update_active_error_component import ApiV1HostsUpdateActiveErrorComponent
        from ..models.api_v1_hosts_update_alias_error_component import ApiV1HostsUpdateAliasErrorComponent
        from ..models.api_v1_hosts_update_annotations_error_component import ApiV1HostsUpdateAnnotationsErrorComponent
        from ..models.api_v1_hosts_update_archived_at_error_component import ApiV1HostsUpdateArchivedAtErrorComponent
        from ..models.api_v1_hosts_update_archived_error_component import ApiV1HostsUpdateArchivedErrorComponent
        from ..models.api_v1_hosts_update_archived_reason_error_component import (
            ApiV1HostsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_update_created_by_component_error_component import (
            ApiV1HostsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_update_credential_error_component import ApiV1HostsUpdateCredentialErrorComponent
        from ..models.api_v1_hosts_update_criticality_error_component import ApiV1HostsUpdateCriticalityErrorComponent
        from ..models.api_v1_hosts_update_debug_mode_error_component import ApiV1HostsUpdateDebugModeErrorComponent
        from ..models.api_v1_hosts_update_default_ipv_4_error_component import ApiV1HostsUpdateDefaultIpv4ErrorComponent
        from ..models.api_v1_hosts_update_default_ipv_6_error_component import ApiV1HostsUpdateDefaultIpv6ErrorComponent
        from ..models.api_v1_hosts_update_description_error_component import ApiV1HostsUpdateDescriptionErrorComponent
        from ..models.api_v1_hosts_update_display_name_error_component import ApiV1HostsUpdateDisplayNameErrorComponent
        from ..models.api_v1_hosts_update_hostname_error_component import ApiV1HostsUpdateHostnameErrorComponent
        from ..models.api_v1_hosts_update_k8s_cluster_error_component import ApiV1HostsUpdateK8SClusterErrorComponent
        from ..models.api_v1_hosts_update_kind_error_component import ApiV1HostsUpdateKindErrorComponent
        from ..models.api_v1_hosts_update_labels_error_component import ApiV1HostsUpdateLabelsErrorComponent
        from ..models.api_v1_hosts_update_name_error_component import ApiV1HostsUpdateNameErrorComponent
        from ..models.api_v1_hosts_update_non_field_errors_error_component import (
            ApiV1HostsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_update_platform_service_error_component import (
            ApiV1HostsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_account_id_error_component import (
            ApiV1HostsUpdateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_error_component import ApiV1HostsUpdateProviderErrorComponent
        from ..models.api_v1_hosts_update_provider_image_error_component import (
            ApiV1HostsUpdateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_image_os_architecture_error_component import (
            ApiV1HostsUpdateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_image_os_flavor_error_component import (
            ApiV1HostsUpdateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_image_os_version_error_component import (
            ApiV1HostsUpdateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_location_error_component import (
            ApiV1HostsUpdateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_reference_error_component import (
            ApiV1HostsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_type_error_component import (
            ApiV1HostsUpdateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_update_reconciliation_enabled_error_component import (
            ApiV1HostsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_update_resource_cpu_architecture_error_component import (
            ApiV1HostsUpdateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_update_resource_cpu_cores_error_component import (
            ApiV1HostsUpdateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_update_resource_cpu_type_error_component import (
            ApiV1HostsUpdateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_update_resource_disk_error_component import (
            ApiV1HostsUpdateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_update_resource_memory_error_component import (
            ApiV1HostsUpdateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_update_role_error_component import ApiV1HostsUpdateRoleErrorComponent
        from ..models.api_v1_hosts_update_sla_availability_error_component import (
            ApiV1HostsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_update_sla_target_error_component import ApiV1HostsUpdateSlaTargetErrorComponent
        from ..models.api_v1_hosts_update_slo_availability_error_component import (
            ApiV1HostsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_update_slo_target_error_component import ApiV1HostsUpdateSloTargetErrorComponent
        from ..models.api_v1_hosts_update_ssh_keys_id_error_component import ApiV1HostsUpdateSshKeysIdErrorComponent
        from ..models.api_v1_hosts_update_target_availability_error_component import (
            ApiV1HostsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_update_tolerations_error_component import ApiV1HostsUpdateTolerationsErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1HostsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateDefaultIpv4ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateDefaultIpv6ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateResourceCpuTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateResourceCpuCoresErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateResourceCpuArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateResourceMemoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateResourceDiskErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateProviderLocationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateProviderImageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateProviderImageOsFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateProviderImageOsVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateProviderImageOsArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateProviderTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateProviderAccountIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateSshKeysIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsUpdateK8SClusterErrorComponent):
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
        from ..models.api_v1_hosts_update_active_error_component import ApiV1HostsUpdateActiveErrorComponent
        from ..models.api_v1_hosts_update_alias_error_component import ApiV1HostsUpdateAliasErrorComponent
        from ..models.api_v1_hosts_update_annotations_error_component import ApiV1HostsUpdateAnnotationsErrorComponent
        from ..models.api_v1_hosts_update_archived_at_error_component import ApiV1HostsUpdateArchivedAtErrorComponent
        from ..models.api_v1_hosts_update_archived_error_component import ApiV1HostsUpdateArchivedErrorComponent
        from ..models.api_v1_hosts_update_archived_reason_error_component import (
            ApiV1HostsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_update_created_by_component_error_component import (
            ApiV1HostsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_update_credential_error_component import ApiV1HostsUpdateCredentialErrorComponent
        from ..models.api_v1_hosts_update_criticality_error_component import ApiV1HostsUpdateCriticalityErrorComponent
        from ..models.api_v1_hosts_update_debug_mode_error_component import ApiV1HostsUpdateDebugModeErrorComponent
        from ..models.api_v1_hosts_update_default_ipv_4_error_component import ApiV1HostsUpdateDefaultIpv4ErrorComponent
        from ..models.api_v1_hosts_update_default_ipv_6_error_component import ApiV1HostsUpdateDefaultIpv6ErrorComponent
        from ..models.api_v1_hosts_update_description_error_component import ApiV1HostsUpdateDescriptionErrorComponent
        from ..models.api_v1_hosts_update_display_name_error_component import ApiV1HostsUpdateDisplayNameErrorComponent
        from ..models.api_v1_hosts_update_hostname_error_component import ApiV1HostsUpdateHostnameErrorComponent
        from ..models.api_v1_hosts_update_k8s_cluster_error_component import ApiV1HostsUpdateK8SClusterErrorComponent
        from ..models.api_v1_hosts_update_kind_error_component import ApiV1HostsUpdateKindErrorComponent
        from ..models.api_v1_hosts_update_labels_error_component import ApiV1HostsUpdateLabelsErrorComponent
        from ..models.api_v1_hosts_update_name_error_component import ApiV1HostsUpdateNameErrorComponent
        from ..models.api_v1_hosts_update_non_field_errors_error_component import (
            ApiV1HostsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_update_platform_service_error_component import (
            ApiV1HostsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_update_product_id_error_component import ApiV1HostsUpdateProductIdErrorComponent
        from ..models.api_v1_hosts_update_provider_account_id_error_component import (
            ApiV1HostsUpdateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_error_component import ApiV1HostsUpdateProviderErrorComponent
        from ..models.api_v1_hosts_update_provider_image_error_component import (
            ApiV1HostsUpdateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_image_os_architecture_error_component import (
            ApiV1HostsUpdateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_image_os_flavor_error_component import (
            ApiV1HostsUpdateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_image_os_version_error_component import (
            ApiV1HostsUpdateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_location_error_component import (
            ApiV1HostsUpdateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_reference_error_component import (
            ApiV1HostsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_update_provider_type_error_component import (
            ApiV1HostsUpdateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_update_reconciliation_enabled_error_component import (
            ApiV1HostsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_update_resource_cpu_architecture_error_component import (
            ApiV1HostsUpdateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_update_resource_cpu_cores_error_component import (
            ApiV1HostsUpdateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_update_resource_cpu_type_error_component import (
            ApiV1HostsUpdateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_update_resource_disk_error_component import (
            ApiV1HostsUpdateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_update_resource_memory_error_component import (
            ApiV1HostsUpdateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_update_role_error_component import ApiV1HostsUpdateRoleErrorComponent
        from ..models.api_v1_hosts_update_sla_availability_error_component import (
            ApiV1HostsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_update_sla_target_error_component import ApiV1HostsUpdateSlaTargetErrorComponent
        from ..models.api_v1_hosts_update_slo_availability_error_component import (
            ApiV1HostsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_update_slo_target_error_component import ApiV1HostsUpdateSloTargetErrorComponent
        from ..models.api_v1_hosts_update_ssh_keys_id_error_component import ApiV1HostsUpdateSshKeysIdErrorComponent
        from ..models.api_v1_hosts_update_target_availability_error_component import (
            ApiV1HostsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_update_tolerations_error_component import ApiV1HostsUpdateTolerationsErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1HostsUpdateActiveErrorComponent
                | ApiV1HostsUpdateAliasErrorComponent
                | ApiV1HostsUpdateAnnotationsErrorComponent
                | ApiV1HostsUpdateArchivedAtErrorComponent
                | ApiV1HostsUpdateArchivedErrorComponent
                | ApiV1HostsUpdateArchivedReasonErrorComponent
                | ApiV1HostsUpdateCreatedByComponentErrorComponent
                | ApiV1HostsUpdateCredentialErrorComponent
                | ApiV1HostsUpdateCriticalityErrorComponent
                | ApiV1HostsUpdateDebugModeErrorComponent
                | ApiV1HostsUpdateDefaultIpv4ErrorComponent
                | ApiV1HostsUpdateDefaultIpv6ErrorComponent
                | ApiV1HostsUpdateDescriptionErrorComponent
                | ApiV1HostsUpdateDisplayNameErrorComponent
                | ApiV1HostsUpdateHostnameErrorComponent
                | ApiV1HostsUpdateK8SClusterErrorComponent
                | ApiV1HostsUpdateKindErrorComponent
                | ApiV1HostsUpdateLabelsErrorComponent
                | ApiV1HostsUpdateNameErrorComponent
                | ApiV1HostsUpdateNonFieldErrorsErrorComponent
                | ApiV1HostsUpdatePlatformServiceErrorComponent
                | ApiV1HostsUpdateProductIdErrorComponent
                | ApiV1HostsUpdateProviderAccountIdErrorComponent
                | ApiV1HostsUpdateProviderErrorComponent
                | ApiV1HostsUpdateProviderImageErrorComponent
                | ApiV1HostsUpdateProviderImageOsArchitectureErrorComponent
                | ApiV1HostsUpdateProviderImageOsFlavorErrorComponent
                | ApiV1HostsUpdateProviderImageOsVersionErrorComponent
                | ApiV1HostsUpdateProviderLocationErrorComponent
                | ApiV1HostsUpdateProviderReferenceErrorComponent
                | ApiV1HostsUpdateProviderTypeErrorComponent
                | ApiV1HostsUpdateReconciliationEnabledErrorComponent
                | ApiV1HostsUpdateResourceCpuArchitectureErrorComponent
                | ApiV1HostsUpdateResourceCpuCoresErrorComponent
                | ApiV1HostsUpdateResourceCpuTypeErrorComponent
                | ApiV1HostsUpdateResourceDiskErrorComponent
                | ApiV1HostsUpdateResourceMemoryErrorComponent
                | ApiV1HostsUpdateRoleErrorComponent
                | ApiV1HostsUpdateSlaAvailabilityErrorComponent
                | ApiV1HostsUpdateSlaTargetErrorComponent
                | ApiV1HostsUpdateSloAvailabilityErrorComponent
                | ApiV1HostsUpdateSloTargetErrorComponent
                | ApiV1HostsUpdateSshKeysIdErrorComponent
                | ApiV1HostsUpdateTargetAvailabilityErrorComponent
                | ApiV1HostsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_0 = (
                        ApiV1HostsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_1 = ApiV1HostsUpdateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_2 = (
                        ApiV1HostsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_3 = ApiV1HostsUpdateLabelsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_4 = (
                        ApiV1HostsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_5 = (
                        ApiV1HostsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_6 = (
                        ApiV1HostsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_7 = (
                        ApiV1HostsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_8 = (
                        ApiV1HostsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_9 = (
                        ApiV1HostsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_10 = ApiV1HostsUpdateKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_11 = (
                        ApiV1HostsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_12 = (
                        ApiV1HostsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_13 = (
                        ApiV1HostsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_14 = (
                        ApiV1HostsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_15 = (
                        ApiV1HostsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_16 = (
                        ApiV1HostsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_17 = (
                        ApiV1HostsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_18 = (
                        ApiV1HostsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_19 = (
                        ApiV1HostsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_20 = (
                        ApiV1HostsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_21 = (
                        ApiV1HostsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_22 = (
                        ApiV1HostsUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_23 = ApiV1HostsUpdateAliasErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_24 = ApiV1HostsUpdateRoleErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_25 = (
                        ApiV1HostsUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_26 = (
                        ApiV1HostsUpdateDefaultIpv4ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_27 = (
                        ApiV1HostsUpdateDefaultIpv6ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_28 = (
                        ApiV1HostsUpdateResourceCpuTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_29 = (
                        ApiV1HostsUpdateResourceCpuCoresErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_30 = (
                        ApiV1HostsUpdateResourceCpuArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_31 = (
                        ApiV1HostsUpdateResourceMemoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_32 = (
                        ApiV1HostsUpdateResourceDiskErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_33 = (
                        ApiV1HostsUpdateProviderLocationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_34 = (
                        ApiV1HostsUpdateProviderImageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_35 = (
                        ApiV1HostsUpdateProviderImageOsFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_36 = (
                        ApiV1HostsUpdateProviderImageOsVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_37 = (
                        ApiV1HostsUpdateProviderImageOsArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_38 = (
                        ApiV1HostsUpdateProviderTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_39 = (
                        ApiV1HostsUpdateProviderAccountIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_40 = (
                        ApiV1HostsUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_41 = (
                        ApiV1HostsUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_42 = (
                        ApiV1HostsUpdateSshKeysIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_update_error_type_43 = (
                        ApiV1HostsUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_hosts_update_error_type_44 = ApiV1HostsUpdateProductIdErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_hosts_update_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_hosts_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_hosts_update_validation_error.additional_properties = d
        return api_v1_hosts_update_validation_error

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
