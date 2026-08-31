from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_volumes_update_access_modes_error_component import (
        ApiV1KubernetesVolumesUpdateAccessModesErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_actual_availability_error_component import (
        ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_annotations_error_component import (
        ApiV1KubernetesVolumesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_archived_at_error_component import (
        ApiV1KubernetesVolumesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_archived_error_component import (
        ApiV1KubernetesVolumesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_archived_reason_error_component import (
        ApiV1KubernetesVolumesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_capacity_bytes_error_component import (
        ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_capacity_string_error_component import (
        ApiV1KubernetesVolumesUpdateCapacityStringErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_cloud_provider_volume_id_error_component import (
        ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_criticality_error_component import (
        ApiV1KubernetesVolumesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_csi_driver_error_component import (
        ApiV1KubernetesVolumesUpdateCsiDriverErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_debug_mode_error_component import (
        ApiV1KubernetesVolumesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_discovery_enabled_error_component import (
        ApiV1KubernetesVolumesUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_display_name_error_component import (
        ApiV1KubernetesVolumesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_k8s_app_error_component import (
        ApiV1KubernetesVolumesUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_k8s_cluster_error_component import (
        ApiV1KubernetesVolumesUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_kind_error_component import (
        ApiV1KubernetesVolumesUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_labels_error_component import (
        ApiV1KubernetesVolumesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_managed_by_content_type_error_component import (
        ApiV1KubernetesVolumesUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_managed_by_object_id_error_component import (
        ApiV1KubernetesVolumesUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_name_error_component import (
        ApiV1KubernetesVolumesUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_node_affinity_error_component import (
        ApiV1KubernetesVolumesUpdateNodeAffinityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_non_field_errors_error_component import (
        ApiV1KubernetesVolumesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_phase_error_component import (
        ApiV1KubernetesVolumesUpdatePhaseErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_platform_service_error_component import (
        ApiV1KubernetesVolumesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_provider_error_component import (
        ApiV1KubernetesVolumesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_provider_id_error_component import (
        ApiV1KubernetesVolumesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_provider_object_id_error_component import (
        ApiV1KubernetesVolumesUpdateProviderObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_provider_object_name_error_component import (
        ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_provider_reference_error_component import (
        ApiV1KubernetesVolumesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_pvc_name_error_component import (
        ApiV1KubernetesVolumesUpdatePvcNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_pvc_namespace_error_component import (
        ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_reclaim_policy_error_component import (
        ApiV1KubernetesVolumesUpdateReclaimPolicyErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesVolumesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_scope_error_component import (
        ApiV1KubernetesVolumesUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_sla_availability_error_component import (
        ApiV1KubernetesVolumesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_sla_target_error_component import (
        ApiV1KubernetesVolumesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_slo_availability_error_component import (
        ApiV1KubernetesVolumesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_slo_target_error_component import (
        ApiV1KubernetesVolumesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_storage_class_error_component import (
        ApiV1KubernetesVolumesUpdateStorageClassErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_target_availability_error_component import (
        ApiV1KubernetesVolumesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_update_volume_mode_error_component import (
        ApiV1KubernetesVolumesUpdateVolumeModeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesVolumesUpdateValidationError")


@_attrs_define
class ApiV1KubernetesVolumesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesVolumesUpdateAccessModesErrorComponent |
            ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesVolumesUpdateAnnotationsErrorComponent | ApiV1KubernetesVolumesUpdateArchivedAtErrorComponent |
            ApiV1KubernetesVolumesUpdateArchivedErrorComponent | ApiV1KubernetesVolumesUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponent |
            ApiV1KubernetesVolumesUpdateCapacityStringErrorComponent |
            ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponent |
            ApiV1KubernetesVolumesUpdateCriticalityErrorComponent | ApiV1KubernetesVolumesUpdateCsiDriverErrorComponent |
            ApiV1KubernetesVolumesUpdateDebugModeErrorComponent | ApiV1KubernetesVolumesUpdateDiscoveryEnabledErrorComponent
            | ApiV1KubernetesVolumesUpdateDisplayNameErrorComponent | ApiV1KubernetesVolumesUpdateK8SAppErrorComponent |
            ApiV1KubernetesVolumesUpdateK8SClusterErrorComponent | ApiV1KubernetesVolumesUpdateKindErrorComponent |
            ApiV1KubernetesVolumesUpdateLabelsErrorComponent |
            ApiV1KubernetesVolumesUpdateManagedByContentTypeErrorComponent |
            ApiV1KubernetesVolumesUpdateManagedByObjectIdErrorComponent | ApiV1KubernetesVolumesUpdateNameErrorComponent |
            ApiV1KubernetesVolumesUpdateNodeAffinityErrorComponent |
            ApiV1KubernetesVolumesUpdateNonFieldErrorsErrorComponent | ApiV1KubernetesVolumesUpdatePhaseErrorComponent |
            ApiV1KubernetesVolumesUpdatePlatformServiceErrorComponent | ApiV1KubernetesVolumesUpdateProviderErrorComponent |
            ApiV1KubernetesVolumesUpdateProviderIdErrorComponent |
            ApiV1KubernetesVolumesUpdateProviderObjectIdErrorComponent |
            ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponent |
            ApiV1KubernetesVolumesUpdateProviderReferenceErrorComponent | ApiV1KubernetesVolumesUpdatePvcNameErrorComponent
            | ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponent |
            ApiV1KubernetesVolumesUpdateReclaimPolicyErrorComponent |
            ApiV1KubernetesVolumesUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesVolumesUpdateScopeErrorComponent | ApiV1KubernetesVolumesUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesVolumesUpdateSlaTargetErrorComponent | ApiV1KubernetesVolumesUpdateSloAvailabilityErrorComponent
            | ApiV1KubernetesVolumesUpdateSloTargetErrorComponent | ApiV1KubernetesVolumesUpdateStorageClassErrorComponent |
            ApiV1KubernetesVolumesUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesVolumesUpdateVolumeModeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesVolumesUpdateAccessModesErrorComponent
        | ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesVolumesUpdateAnnotationsErrorComponent
        | ApiV1KubernetesVolumesUpdateArchivedAtErrorComponent
        | ApiV1KubernetesVolumesUpdateArchivedErrorComponent
        | ApiV1KubernetesVolumesUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponent
        | ApiV1KubernetesVolumesUpdateCapacityStringErrorComponent
        | ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponent
        | ApiV1KubernetesVolumesUpdateCriticalityErrorComponent
        | ApiV1KubernetesVolumesUpdateCsiDriverErrorComponent
        | ApiV1KubernetesVolumesUpdateDebugModeErrorComponent
        | ApiV1KubernetesVolumesUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesVolumesUpdateDisplayNameErrorComponent
        | ApiV1KubernetesVolumesUpdateK8SAppErrorComponent
        | ApiV1KubernetesVolumesUpdateK8SClusterErrorComponent
        | ApiV1KubernetesVolumesUpdateKindErrorComponent
        | ApiV1KubernetesVolumesUpdateLabelsErrorComponent
        | ApiV1KubernetesVolumesUpdateManagedByContentTypeErrorComponent
        | ApiV1KubernetesVolumesUpdateManagedByObjectIdErrorComponent
        | ApiV1KubernetesVolumesUpdateNameErrorComponent
        | ApiV1KubernetesVolumesUpdateNodeAffinityErrorComponent
        | ApiV1KubernetesVolumesUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesVolumesUpdatePhaseErrorComponent
        | ApiV1KubernetesVolumesUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesVolumesUpdateProviderErrorComponent
        | ApiV1KubernetesVolumesUpdateProviderIdErrorComponent
        | ApiV1KubernetesVolumesUpdateProviderObjectIdErrorComponent
        | ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponent
        | ApiV1KubernetesVolumesUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesVolumesUpdatePvcNameErrorComponent
        | ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponent
        | ApiV1KubernetesVolumesUpdateReclaimPolicyErrorComponent
        | ApiV1KubernetesVolumesUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesVolumesUpdateScopeErrorComponent
        | ApiV1KubernetesVolumesUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesVolumesUpdateSlaTargetErrorComponent
        | ApiV1KubernetesVolumesUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesVolumesUpdateSloTargetErrorComponent
        | ApiV1KubernetesVolumesUpdateStorageClassErrorComponent
        | ApiV1KubernetesVolumesUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesVolumesUpdateVolumeModeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_volumes_update_access_modes_error_component import (
            ApiV1KubernetesVolumesUpdateAccessModesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_actual_availability_error_component import (
            ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_annotations_error_component import (
            ApiV1KubernetesVolumesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_archived_at_error_component import (
            ApiV1KubernetesVolumesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_archived_error_component import (
            ApiV1KubernetesVolumesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_archived_reason_error_component import (
            ApiV1KubernetesVolumesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_capacity_bytes_error_component import (
            ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_capacity_string_error_component import (
            ApiV1KubernetesVolumesUpdateCapacityStringErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_cloud_provider_volume_id_error_component import (
            ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_criticality_error_component import (
            ApiV1KubernetesVolumesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_csi_driver_error_component import (
            ApiV1KubernetesVolumesUpdateCsiDriverErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_debug_mode_error_component import (
            ApiV1KubernetesVolumesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_discovery_enabled_error_component import (
            ApiV1KubernetesVolumesUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_display_name_error_component import (
            ApiV1KubernetesVolumesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_k8s_app_error_component import (
            ApiV1KubernetesVolumesUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_k8s_cluster_error_component import (
            ApiV1KubernetesVolumesUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_kind_error_component import (
            ApiV1KubernetesVolumesUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_labels_error_component import (
            ApiV1KubernetesVolumesUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_managed_by_content_type_error_component import (
            ApiV1KubernetesVolumesUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_name_error_component import (
            ApiV1KubernetesVolumesUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_node_affinity_error_component import (
            ApiV1KubernetesVolumesUpdateNodeAffinityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_non_field_errors_error_component import (
            ApiV1KubernetesVolumesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_phase_error_component import (
            ApiV1KubernetesVolumesUpdatePhaseErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_platform_service_error_component import (
            ApiV1KubernetesVolumesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_provider_error_component import (
            ApiV1KubernetesVolumesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_provider_id_error_component import (
            ApiV1KubernetesVolumesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_provider_object_id_error_component import (
            ApiV1KubernetesVolumesUpdateProviderObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_provider_object_name_error_component import (
            ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_provider_reference_error_component import (
            ApiV1KubernetesVolumesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_pvc_name_error_component import (
            ApiV1KubernetesVolumesUpdatePvcNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_pvc_namespace_error_component import (
            ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_reclaim_policy_error_component import (
            ApiV1KubernetesVolumesUpdateReclaimPolicyErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesVolumesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_scope_error_component import (
            ApiV1KubernetesVolumesUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_sla_availability_error_component import (
            ApiV1KubernetesVolumesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_sla_target_error_component import (
            ApiV1KubernetesVolumesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_slo_availability_error_component import (
            ApiV1KubernetesVolumesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_slo_target_error_component import (
            ApiV1KubernetesVolumesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_storage_class_error_component import (
            ApiV1KubernetesVolumesUpdateStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_target_availability_error_component import (
            ApiV1KubernetesVolumesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_volume_mode_error_component import (
            ApiV1KubernetesVolumesUpdateVolumeModeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateProviderObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateCsiDriverErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateCapacityStringErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdatePhaseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateAccessModesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateVolumeModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateReclaimPolicyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdatePvcNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateNodeAffinityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesUpdateManagedByContentTypeErrorComponent):
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
        from ..models.api_v1_kubernetes_volumes_update_access_modes_error_component import (
            ApiV1KubernetesVolumesUpdateAccessModesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_actual_availability_error_component import (
            ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_annotations_error_component import (
            ApiV1KubernetesVolumesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_archived_at_error_component import (
            ApiV1KubernetesVolumesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_archived_error_component import (
            ApiV1KubernetesVolumesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_archived_reason_error_component import (
            ApiV1KubernetesVolumesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_capacity_bytes_error_component import (
            ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_capacity_string_error_component import (
            ApiV1KubernetesVolumesUpdateCapacityStringErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_cloud_provider_volume_id_error_component import (
            ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_criticality_error_component import (
            ApiV1KubernetesVolumesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_csi_driver_error_component import (
            ApiV1KubernetesVolumesUpdateCsiDriverErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_debug_mode_error_component import (
            ApiV1KubernetesVolumesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_discovery_enabled_error_component import (
            ApiV1KubernetesVolumesUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_display_name_error_component import (
            ApiV1KubernetesVolumesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_k8s_app_error_component import (
            ApiV1KubernetesVolumesUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_k8s_cluster_error_component import (
            ApiV1KubernetesVolumesUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_kind_error_component import (
            ApiV1KubernetesVolumesUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_labels_error_component import (
            ApiV1KubernetesVolumesUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_managed_by_content_type_error_component import (
            ApiV1KubernetesVolumesUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_managed_by_object_id_error_component import (
            ApiV1KubernetesVolumesUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_name_error_component import (
            ApiV1KubernetesVolumesUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_node_affinity_error_component import (
            ApiV1KubernetesVolumesUpdateNodeAffinityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_non_field_errors_error_component import (
            ApiV1KubernetesVolumesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_phase_error_component import (
            ApiV1KubernetesVolumesUpdatePhaseErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_platform_service_error_component import (
            ApiV1KubernetesVolumesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_provider_error_component import (
            ApiV1KubernetesVolumesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_provider_id_error_component import (
            ApiV1KubernetesVolumesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_provider_object_id_error_component import (
            ApiV1KubernetesVolumesUpdateProviderObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_provider_object_name_error_component import (
            ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_provider_reference_error_component import (
            ApiV1KubernetesVolumesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_pvc_name_error_component import (
            ApiV1KubernetesVolumesUpdatePvcNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_pvc_namespace_error_component import (
            ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_reclaim_policy_error_component import (
            ApiV1KubernetesVolumesUpdateReclaimPolicyErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesVolumesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_scope_error_component import (
            ApiV1KubernetesVolumesUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_sla_availability_error_component import (
            ApiV1KubernetesVolumesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_sla_target_error_component import (
            ApiV1KubernetesVolumesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_slo_availability_error_component import (
            ApiV1KubernetesVolumesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_slo_target_error_component import (
            ApiV1KubernetesVolumesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_storage_class_error_component import (
            ApiV1KubernetesVolumesUpdateStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_target_availability_error_component import (
            ApiV1KubernetesVolumesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_update_volume_mode_error_component import (
            ApiV1KubernetesVolumesUpdateVolumeModeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesVolumesUpdateAccessModesErrorComponent
                | ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesVolumesUpdateAnnotationsErrorComponent
                | ApiV1KubernetesVolumesUpdateArchivedAtErrorComponent
                | ApiV1KubernetesVolumesUpdateArchivedErrorComponent
                | ApiV1KubernetesVolumesUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponent
                | ApiV1KubernetesVolumesUpdateCapacityStringErrorComponent
                | ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponent
                | ApiV1KubernetesVolumesUpdateCriticalityErrorComponent
                | ApiV1KubernetesVolumesUpdateCsiDriverErrorComponent
                | ApiV1KubernetesVolumesUpdateDebugModeErrorComponent
                | ApiV1KubernetesVolumesUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesVolumesUpdateDisplayNameErrorComponent
                | ApiV1KubernetesVolumesUpdateK8SAppErrorComponent
                | ApiV1KubernetesVolumesUpdateK8SClusterErrorComponent
                | ApiV1KubernetesVolumesUpdateKindErrorComponent
                | ApiV1KubernetesVolumesUpdateLabelsErrorComponent
                | ApiV1KubernetesVolumesUpdateManagedByContentTypeErrorComponent
                | ApiV1KubernetesVolumesUpdateManagedByObjectIdErrorComponent
                | ApiV1KubernetesVolumesUpdateNameErrorComponent
                | ApiV1KubernetesVolumesUpdateNodeAffinityErrorComponent
                | ApiV1KubernetesVolumesUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesVolumesUpdatePhaseErrorComponent
                | ApiV1KubernetesVolumesUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesVolumesUpdateProviderErrorComponent
                | ApiV1KubernetesVolumesUpdateProviderIdErrorComponent
                | ApiV1KubernetesVolumesUpdateProviderObjectIdErrorComponent
                | ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponent
                | ApiV1KubernetesVolumesUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesVolumesUpdatePvcNameErrorComponent
                | ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponent
                | ApiV1KubernetesVolumesUpdateReclaimPolicyErrorComponent
                | ApiV1KubernetesVolumesUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesVolumesUpdateScopeErrorComponent
                | ApiV1KubernetesVolumesUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesVolumesUpdateSlaTargetErrorComponent
                | ApiV1KubernetesVolumesUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesVolumesUpdateSloTargetErrorComponent
                | ApiV1KubernetesVolumesUpdateStorageClassErrorComponent
                | ApiV1KubernetesVolumesUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesVolumesUpdateVolumeModeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_0 = (
                        ApiV1KubernetesVolumesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_1 = (
                        ApiV1KubernetesVolumesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_2 = (
                        ApiV1KubernetesVolumesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_3 = (
                        ApiV1KubernetesVolumesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_4 = (
                        ApiV1KubernetesVolumesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_5 = (
                        ApiV1KubernetesVolumesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_6 = (
                        ApiV1KubernetesVolumesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_7 = (
                        ApiV1KubernetesVolumesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_8 = (
                        ApiV1KubernetesVolumesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_9 = (
                        ApiV1KubernetesVolumesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_10 = (
                        ApiV1KubernetesVolumesUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_11 = (
                        ApiV1KubernetesVolumesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_12 = (
                        ApiV1KubernetesVolumesUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_13 = (
                        ApiV1KubernetesVolumesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_14 = (
                        ApiV1KubernetesVolumesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_15 = (
                        ApiV1KubernetesVolumesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_16 = (
                        ApiV1KubernetesVolumesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_17 = (
                        ApiV1KubernetesVolumesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_18 = (
                        ApiV1KubernetesVolumesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_19 = (
                        ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_20 = (
                        ApiV1KubernetesVolumesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_21 = (
                        ApiV1KubernetesVolumesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_22 = (
                        ApiV1KubernetesVolumesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_23 = (
                        ApiV1KubernetesVolumesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_24 = (
                        ApiV1KubernetesVolumesUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_25 = (
                        ApiV1KubernetesVolumesUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_26 = (
                        ApiV1KubernetesVolumesUpdateProviderObjectNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_27 = (
                        ApiV1KubernetesVolumesUpdateProviderObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_28 = (
                        ApiV1KubernetesVolumesUpdateCloudProviderVolumeIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_29 = (
                        ApiV1KubernetesVolumesUpdateCsiDriverErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_30 = (
                        ApiV1KubernetesVolumesUpdateStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_31 = (
                        ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_32 = (
                        ApiV1KubernetesVolumesUpdateCapacityStringErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_33 = (
                        ApiV1KubernetesVolumesUpdatePhaseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_34 = (
                        ApiV1KubernetesVolumesUpdateAccessModesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_35 = (
                        ApiV1KubernetesVolumesUpdateVolumeModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_36 = (
                        ApiV1KubernetesVolumesUpdateReclaimPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_37 = (
                        ApiV1KubernetesVolumesUpdatePvcNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_38 = (
                        ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_39 = (
                        ApiV1KubernetesVolumesUpdateNodeAffinityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_update_error_type_40 = (
                        ApiV1KubernetesVolumesUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_volumes_update_error_type_41 = (
                    ApiV1KubernetesVolumesUpdateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_volumes_update_error_type_41

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_volumes_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_volumes_update_validation_error.additional_properties = d
        return api_v1_kubernetes_volumes_update_validation_error

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
