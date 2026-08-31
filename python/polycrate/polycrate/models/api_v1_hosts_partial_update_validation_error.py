from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_hosts_partial_update_active_error_component import ApiV1HostsPartialUpdateActiveErrorComponent
    from ..models.api_v1_hosts_partial_update_alias_error_component import ApiV1HostsPartialUpdateAliasErrorComponent
    from ..models.api_v1_hosts_partial_update_annotations_error_component import (
        ApiV1HostsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_archived_at_error_component import (
        ApiV1HostsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_archived_error_component import (
        ApiV1HostsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_archived_reason_error_component import (
        ApiV1HostsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_created_by_component_error_component import (
        ApiV1HostsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_credential_error_component import (
        ApiV1HostsPartialUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_criticality_error_component import (
        ApiV1HostsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_debug_mode_error_component import (
        ApiV1HostsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_default_ipv_4_error_component import (
        ApiV1HostsPartialUpdateDefaultIpv4ErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_default_ipv_6_error_component import (
        ApiV1HostsPartialUpdateDefaultIpv6ErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_description_error_component import (
        ApiV1HostsPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_display_name_error_component import (
        ApiV1HostsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_hostname_error_component import (
        ApiV1HostsPartialUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_k8s_cluster_error_component import (
        ApiV1HostsPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_kind_error_component import ApiV1HostsPartialUpdateKindErrorComponent
    from ..models.api_v1_hosts_partial_update_labels_error_component import ApiV1HostsPartialUpdateLabelsErrorComponent
    from ..models.api_v1_hosts_partial_update_name_error_component import ApiV1HostsPartialUpdateNameErrorComponent
    from ..models.api_v1_hosts_partial_update_non_field_errors_error_component import (
        ApiV1HostsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_platform_service_error_component import (
        ApiV1HostsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_product_id_error_component import (
        ApiV1HostsPartialUpdateProductIdErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_provider_account_id_error_component import (
        ApiV1HostsPartialUpdateProviderAccountIdErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_provider_error_component import (
        ApiV1HostsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_provider_image_error_component import (
        ApiV1HostsPartialUpdateProviderImageErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_provider_image_os_architecture_error_component import (
        ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_provider_image_os_flavor_error_component import (
        ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_provider_image_os_version_error_component import (
        ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_provider_location_error_component import (
        ApiV1HostsPartialUpdateProviderLocationErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_provider_reference_error_component import (
        ApiV1HostsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_provider_type_error_component import (
        ApiV1HostsPartialUpdateProviderTypeErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_reconciliation_enabled_error_component import (
        ApiV1HostsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_resource_cpu_architecture_error_component import (
        ApiV1HostsPartialUpdateResourceCpuArchitectureErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_resource_cpu_cores_error_component import (
        ApiV1HostsPartialUpdateResourceCpuCoresErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_resource_cpu_type_error_component import (
        ApiV1HostsPartialUpdateResourceCpuTypeErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_resource_disk_error_component import (
        ApiV1HostsPartialUpdateResourceDiskErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_resource_memory_error_component import (
        ApiV1HostsPartialUpdateResourceMemoryErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_role_error_component import ApiV1HostsPartialUpdateRoleErrorComponent
    from ..models.api_v1_hosts_partial_update_sla_availability_error_component import (
        ApiV1HostsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_sla_target_error_component import (
        ApiV1HostsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_slo_availability_error_component import (
        ApiV1HostsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_slo_target_error_component import (
        ApiV1HostsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_ssh_keys_id_error_component import (
        ApiV1HostsPartialUpdateSshKeysIdErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_target_availability_error_component import (
        ApiV1HostsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_hosts_partial_update_tolerations_error_component import (
        ApiV1HostsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1HostsPartialUpdateValidationError")


@_attrs_define
class ApiV1HostsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1HostsPartialUpdateActiveErrorComponent | ApiV1HostsPartialUpdateAliasErrorComponent |
            ApiV1HostsPartialUpdateAnnotationsErrorComponent | ApiV1HostsPartialUpdateArchivedAtErrorComponent |
            ApiV1HostsPartialUpdateArchivedErrorComponent | ApiV1HostsPartialUpdateArchivedReasonErrorComponent |
            ApiV1HostsPartialUpdateCreatedByComponentErrorComponent | ApiV1HostsPartialUpdateCredentialErrorComponent |
            ApiV1HostsPartialUpdateCriticalityErrorComponent | ApiV1HostsPartialUpdateDebugModeErrorComponent |
            ApiV1HostsPartialUpdateDefaultIpv4ErrorComponent | ApiV1HostsPartialUpdateDefaultIpv6ErrorComponent |
            ApiV1HostsPartialUpdateDescriptionErrorComponent | ApiV1HostsPartialUpdateDisplayNameErrorComponent |
            ApiV1HostsPartialUpdateHostnameErrorComponent | ApiV1HostsPartialUpdateK8SClusterErrorComponent |
            ApiV1HostsPartialUpdateKindErrorComponent | ApiV1HostsPartialUpdateLabelsErrorComponent |
            ApiV1HostsPartialUpdateNameErrorComponent | ApiV1HostsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1HostsPartialUpdatePlatformServiceErrorComponent | ApiV1HostsPartialUpdateProductIdErrorComponent |
            ApiV1HostsPartialUpdateProviderAccountIdErrorComponent | ApiV1HostsPartialUpdateProviderErrorComponent |
            ApiV1HostsPartialUpdateProviderImageErrorComponent |
            ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponent |
            ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponent |
            ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponent |
            ApiV1HostsPartialUpdateProviderLocationErrorComponent | ApiV1HostsPartialUpdateProviderReferenceErrorComponent |
            ApiV1HostsPartialUpdateProviderTypeErrorComponent | ApiV1HostsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1HostsPartialUpdateResourceCpuArchitectureErrorComponent |
            ApiV1HostsPartialUpdateResourceCpuCoresErrorComponent | ApiV1HostsPartialUpdateResourceCpuTypeErrorComponent |
            ApiV1HostsPartialUpdateResourceDiskErrorComponent | ApiV1HostsPartialUpdateResourceMemoryErrorComponent |
            ApiV1HostsPartialUpdateRoleErrorComponent | ApiV1HostsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1HostsPartialUpdateSlaTargetErrorComponent | ApiV1HostsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1HostsPartialUpdateSloTargetErrorComponent | ApiV1HostsPartialUpdateSshKeysIdErrorComponent |
            ApiV1HostsPartialUpdateTargetAvailabilityErrorComponent | ApiV1HostsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1HostsPartialUpdateActiveErrorComponent
        | ApiV1HostsPartialUpdateAliasErrorComponent
        | ApiV1HostsPartialUpdateAnnotationsErrorComponent
        | ApiV1HostsPartialUpdateArchivedAtErrorComponent
        | ApiV1HostsPartialUpdateArchivedErrorComponent
        | ApiV1HostsPartialUpdateArchivedReasonErrorComponent
        | ApiV1HostsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1HostsPartialUpdateCredentialErrorComponent
        | ApiV1HostsPartialUpdateCriticalityErrorComponent
        | ApiV1HostsPartialUpdateDebugModeErrorComponent
        | ApiV1HostsPartialUpdateDefaultIpv4ErrorComponent
        | ApiV1HostsPartialUpdateDefaultIpv6ErrorComponent
        | ApiV1HostsPartialUpdateDescriptionErrorComponent
        | ApiV1HostsPartialUpdateDisplayNameErrorComponent
        | ApiV1HostsPartialUpdateHostnameErrorComponent
        | ApiV1HostsPartialUpdateK8SClusterErrorComponent
        | ApiV1HostsPartialUpdateKindErrorComponent
        | ApiV1HostsPartialUpdateLabelsErrorComponent
        | ApiV1HostsPartialUpdateNameErrorComponent
        | ApiV1HostsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1HostsPartialUpdatePlatformServiceErrorComponent
        | ApiV1HostsPartialUpdateProductIdErrorComponent
        | ApiV1HostsPartialUpdateProviderAccountIdErrorComponent
        | ApiV1HostsPartialUpdateProviderErrorComponent
        | ApiV1HostsPartialUpdateProviderImageErrorComponent
        | ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponent
        | ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponent
        | ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponent
        | ApiV1HostsPartialUpdateProviderLocationErrorComponent
        | ApiV1HostsPartialUpdateProviderReferenceErrorComponent
        | ApiV1HostsPartialUpdateProviderTypeErrorComponent
        | ApiV1HostsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1HostsPartialUpdateResourceCpuArchitectureErrorComponent
        | ApiV1HostsPartialUpdateResourceCpuCoresErrorComponent
        | ApiV1HostsPartialUpdateResourceCpuTypeErrorComponent
        | ApiV1HostsPartialUpdateResourceDiskErrorComponent
        | ApiV1HostsPartialUpdateResourceMemoryErrorComponent
        | ApiV1HostsPartialUpdateRoleErrorComponent
        | ApiV1HostsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1HostsPartialUpdateSlaTargetErrorComponent
        | ApiV1HostsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1HostsPartialUpdateSloTargetErrorComponent
        | ApiV1HostsPartialUpdateSshKeysIdErrorComponent
        | ApiV1HostsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1HostsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_hosts_partial_update_active_error_component import (
            ApiV1HostsPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_alias_error_component import (
            ApiV1HostsPartialUpdateAliasErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_annotations_error_component import (
            ApiV1HostsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_archived_at_error_component import (
            ApiV1HostsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_archived_error_component import (
            ApiV1HostsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_archived_reason_error_component import (
            ApiV1HostsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_created_by_component_error_component import (
            ApiV1HostsPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_credential_error_component import (
            ApiV1HostsPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_criticality_error_component import (
            ApiV1HostsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_debug_mode_error_component import (
            ApiV1HostsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_default_ipv_4_error_component import (
            ApiV1HostsPartialUpdateDefaultIpv4ErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_default_ipv_6_error_component import (
            ApiV1HostsPartialUpdateDefaultIpv6ErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_description_error_component import (
            ApiV1HostsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_display_name_error_component import (
            ApiV1HostsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_hostname_error_component import (
            ApiV1HostsPartialUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_k8s_cluster_error_component import (
            ApiV1HostsPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_kind_error_component import ApiV1HostsPartialUpdateKindErrorComponent
        from ..models.api_v1_hosts_partial_update_labels_error_component import (
            ApiV1HostsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_name_error_component import ApiV1HostsPartialUpdateNameErrorComponent
        from ..models.api_v1_hosts_partial_update_non_field_errors_error_component import (
            ApiV1HostsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_platform_service_error_component import (
            ApiV1HostsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_account_id_error_component import (
            ApiV1HostsPartialUpdateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_error_component import (
            ApiV1HostsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_image_error_component import (
            ApiV1HostsPartialUpdateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_image_os_architecture_error_component import (
            ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_image_os_flavor_error_component import (
            ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_image_os_version_error_component import (
            ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_location_error_component import (
            ApiV1HostsPartialUpdateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_reference_error_component import (
            ApiV1HostsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_type_error_component import (
            ApiV1HostsPartialUpdateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_reconciliation_enabled_error_component import (
            ApiV1HostsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_resource_cpu_architecture_error_component import (
            ApiV1HostsPartialUpdateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_resource_cpu_cores_error_component import (
            ApiV1HostsPartialUpdateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_resource_cpu_type_error_component import (
            ApiV1HostsPartialUpdateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_resource_disk_error_component import (
            ApiV1HostsPartialUpdateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_resource_memory_error_component import (
            ApiV1HostsPartialUpdateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_role_error_component import ApiV1HostsPartialUpdateRoleErrorComponent
        from ..models.api_v1_hosts_partial_update_sla_availability_error_component import (
            ApiV1HostsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_sla_target_error_component import (
            ApiV1HostsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_slo_availability_error_component import (
            ApiV1HostsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_slo_target_error_component import (
            ApiV1HostsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_ssh_keys_id_error_component import (
            ApiV1HostsPartialUpdateSshKeysIdErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_target_availability_error_component import (
            ApiV1HostsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_tolerations_error_component import (
            ApiV1HostsPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1HostsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateDefaultIpv4ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateDefaultIpv6ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateResourceCpuTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateResourceCpuCoresErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateResourceCpuArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateResourceMemoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateResourceDiskErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateProviderLocationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateProviderImageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateProviderTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateProviderAccountIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateSshKeysIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1HostsPartialUpdateK8SClusterErrorComponent):
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
        from ..models.api_v1_hosts_partial_update_active_error_component import (
            ApiV1HostsPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_alias_error_component import (
            ApiV1HostsPartialUpdateAliasErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_annotations_error_component import (
            ApiV1HostsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_archived_at_error_component import (
            ApiV1HostsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_archived_error_component import (
            ApiV1HostsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_archived_reason_error_component import (
            ApiV1HostsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_created_by_component_error_component import (
            ApiV1HostsPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_credential_error_component import (
            ApiV1HostsPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_criticality_error_component import (
            ApiV1HostsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_debug_mode_error_component import (
            ApiV1HostsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_default_ipv_4_error_component import (
            ApiV1HostsPartialUpdateDefaultIpv4ErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_default_ipv_6_error_component import (
            ApiV1HostsPartialUpdateDefaultIpv6ErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_description_error_component import (
            ApiV1HostsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_display_name_error_component import (
            ApiV1HostsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_hostname_error_component import (
            ApiV1HostsPartialUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_k8s_cluster_error_component import (
            ApiV1HostsPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_kind_error_component import ApiV1HostsPartialUpdateKindErrorComponent
        from ..models.api_v1_hosts_partial_update_labels_error_component import (
            ApiV1HostsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_name_error_component import ApiV1HostsPartialUpdateNameErrorComponent
        from ..models.api_v1_hosts_partial_update_non_field_errors_error_component import (
            ApiV1HostsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_platform_service_error_component import (
            ApiV1HostsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_product_id_error_component import (
            ApiV1HostsPartialUpdateProductIdErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_account_id_error_component import (
            ApiV1HostsPartialUpdateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_error_component import (
            ApiV1HostsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_image_error_component import (
            ApiV1HostsPartialUpdateProviderImageErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_image_os_architecture_error_component import (
            ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_image_os_flavor_error_component import (
            ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_image_os_version_error_component import (
            ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_location_error_component import (
            ApiV1HostsPartialUpdateProviderLocationErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_reference_error_component import (
            ApiV1HostsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_provider_type_error_component import (
            ApiV1HostsPartialUpdateProviderTypeErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_reconciliation_enabled_error_component import (
            ApiV1HostsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_resource_cpu_architecture_error_component import (
            ApiV1HostsPartialUpdateResourceCpuArchitectureErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_resource_cpu_cores_error_component import (
            ApiV1HostsPartialUpdateResourceCpuCoresErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_resource_cpu_type_error_component import (
            ApiV1HostsPartialUpdateResourceCpuTypeErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_resource_disk_error_component import (
            ApiV1HostsPartialUpdateResourceDiskErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_resource_memory_error_component import (
            ApiV1HostsPartialUpdateResourceMemoryErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_role_error_component import ApiV1HostsPartialUpdateRoleErrorComponent
        from ..models.api_v1_hosts_partial_update_sla_availability_error_component import (
            ApiV1HostsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_sla_target_error_component import (
            ApiV1HostsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_slo_availability_error_component import (
            ApiV1HostsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_slo_target_error_component import (
            ApiV1HostsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_ssh_keys_id_error_component import (
            ApiV1HostsPartialUpdateSshKeysIdErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_target_availability_error_component import (
            ApiV1HostsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_hosts_partial_update_tolerations_error_component import (
            ApiV1HostsPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1HostsPartialUpdateActiveErrorComponent
                | ApiV1HostsPartialUpdateAliasErrorComponent
                | ApiV1HostsPartialUpdateAnnotationsErrorComponent
                | ApiV1HostsPartialUpdateArchivedAtErrorComponent
                | ApiV1HostsPartialUpdateArchivedErrorComponent
                | ApiV1HostsPartialUpdateArchivedReasonErrorComponent
                | ApiV1HostsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1HostsPartialUpdateCredentialErrorComponent
                | ApiV1HostsPartialUpdateCriticalityErrorComponent
                | ApiV1HostsPartialUpdateDebugModeErrorComponent
                | ApiV1HostsPartialUpdateDefaultIpv4ErrorComponent
                | ApiV1HostsPartialUpdateDefaultIpv6ErrorComponent
                | ApiV1HostsPartialUpdateDescriptionErrorComponent
                | ApiV1HostsPartialUpdateDisplayNameErrorComponent
                | ApiV1HostsPartialUpdateHostnameErrorComponent
                | ApiV1HostsPartialUpdateK8SClusterErrorComponent
                | ApiV1HostsPartialUpdateKindErrorComponent
                | ApiV1HostsPartialUpdateLabelsErrorComponent
                | ApiV1HostsPartialUpdateNameErrorComponent
                | ApiV1HostsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1HostsPartialUpdatePlatformServiceErrorComponent
                | ApiV1HostsPartialUpdateProductIdErrorComponent
                | ApiV1HostsPartialUpdateProviderAccountIdErrorComponent
                | ApiV1HostsPartialUpdateProviderErrorComponent
                | ApiV1HostsPartialUpdateProviderImageErrorComponent
                | ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponent
                | ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponent
                | ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponent
                | ApiV1HostsPartialUpdateProviderLocationErrorComponent
                | ApiV1HostsPartialUpdateProviderReferenceErrorComponent
                | ApiV1HostsPartialUpdateProviderTypeErrorComponent
                | ApiV1HostsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1HostsPartialUpdateResourceCpuArchitectureErrorComponent
                | ApiV1HostsPartialUpdateResourceCpuCoresErrorComponent
                | ApiV1HostsPartialUpdateResourceCpuTypeErrorComponent
                | ApiV1HostsPartialUpdateResourceDiskErrorComponent
                | ApiV1HostsPartialUpdateResourceMemoryErrorComponent
                | ApiV1HostsPartialUpdateRoleErrorComponent
                | ApiV1HostsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1HostsPartialUpdateSlaTargetErrorComponent
                | ApiV1HostsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1HostsPartialUpdateSloTargetErrorComponent
                | ApiV1HostsPartialUpdateSshKeysIdErrorComponent
                | ApiV1HostsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1HostsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_0 = (
                        ApiV1HostsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_1 = (
                        ApiV1HostsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_2 = (
                        ApiV1HostsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_3 = (
                        ApiV1HostsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_4 = (
                        ApiV1HostsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_5 = (
                        ApiV1HostsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_6 = (
                        ApiV1HostsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_7 = (
                        ApiV1HostsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_8 = (
                        ApiV1HostsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_9 = (
                        ApiV1HostsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_10 = (
                        ApiV1HostsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_11 = (
                        ApiV1HostsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_12 = (
                        ApiV1HostsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_13 = (
                        ApiV1HostsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_14 = (
                        ApiV1HostsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_15 = (
                        ApiV1HostsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_16 = (
                        ApiV1HostsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_17 = (
                        ApiV1HostsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_18 = (
                        ApiV1HostsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_19 = (
                        ApiV1HostsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_20 = (
                        ApiV1HostsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_21 = (
                        ApiV1HostsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_22 = (
                        ApiV1HostsPartialUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_23 = (
                        ApiV1HostsPartialUpdateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_24 = (
                        ApiV1HostsPartialUpdateRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_25 = (
                        ApiV1HostsPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_26 = (
                        ApiV1HostsPartialUpdateDefaultIpv4ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_27 = (
                        ApiV1HostsPartialUpdateDefaultIpv6ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_28 = (
                        ApiV1HostsPartialUpdateResourceCpuTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_29 = (
                        ApiV1HostsPartialUpdateResourceCpuCoresErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_30 = (
                        ApiV1HostsPartialUpdateResourceCpuArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_31 = (
                        ApiV1HostsPartialUpdateResourceMemoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_32 = (
                        ApiV1HostsPartialUpdateResourceDiskErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_33 = (
                        ApiV1HostsPartialUpdateProviderLocationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_34 = (
                        ApiV1HostsPartialUpdateProviderImageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_35 = (
                        ApiV1HostsPartialUpdateProviderImageOsFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_36 = (
                        ApiV1HostsPartialUpdateProviderImageOsVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_37 = (
                        ApiV1HostsPartialUpdateProviderImageOsArchitectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_38 = (
                        ApiV1HostsPartialUpdateProviderTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_39 = (
                        ApiV1HostsPartialUpdateProviderAccountIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_40 = (
                        ApiV1HostsPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_41 = (
                        ApiV1HostsPartialUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_42 = (
                        ApiV1HostsPartialUpdateSshKeysIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_hosts_partial_update_error_type_43 = (
                        ApiV1HostsPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_hosts_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_hosts_partial_update_error_type_44 = (
                    ApiV1HostsPartialUpdateProductIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_hosts_partial_update_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_hosts_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_hosts_partial_update_validation_error.additional_properties = d
        return api_v1_hosts_partial_update_validation_error

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
