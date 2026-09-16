from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_volumes_partial_update_access_modes_error_component import (
        ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_actual_availability_error_component import (
        ApiV1KubernetesVolumesPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_annotations_error_component import (
        ApiV1KubernetesVolumesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_archived_at_error_component import (
        ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_archived_error_component import (
        ApiV1KubernetesVolumesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_archived_reason_error_component import (
        ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_capacity_bytes_error_component import (
        ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_capacity_string_error_component import (
        ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_cloud_provider_volume_id_error_component import (
        ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_criticality_error_component import (
        ApiV1KubernetesVolumesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_csi_driver_error_component import (
        ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_debug_mode_error_component import (
        ApiV1KubernetesVolumesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_discovery_enabled_error_component import (
        ApiV1KubernetesVolumesPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_display_name_error_component import (
        ApiV1KubernetesVolumesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_k8s_app_error_component import (
        ApiV1KubernetesVolumesPartialUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_k8s_cluster_error_component import (
        ApiV1KubernetesVolumesPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_kind_error_component import (
        ApiV1KubernetesVolumesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_labels_error_component import (
        ApiV1KubernetesVolumesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_managed_by_content_type_error_component import (
        ApiV1KubernetesVolumesPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_managed_by_object_id_error_component import (
        ApiV1KubernetesVolumesPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_name_error_component import (
        ApiV1KubernetesVolumesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_node_affinity_error_component import (
        ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_non_field_errors_error_component import (
        ApiV1KubernetesVolumesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_phase_error_component import (
        ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_platform_service_error_component import (
        ApiV1KubernetesVolumesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_provider_error_component import (
        ApiV1KubernetesVolumesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_provider_id_error_component import (
        ApiV1KubernetesVolumesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_provider_object_id_error_component import (
        ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_provider_object_name_error_component import (
        ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_provider_reference_error_component import (
        ApiV1KubernetesVolumesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_pvc_name_error_component import (
        ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_pvc_namespace_error_component import (
        ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_reclaim_policy_error_component import (
        ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesVolumesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_scope_error_component import (
        ApiV1KubernetesVolumesPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_sla_availability_error_component import (
        ApiV1KubernetesVolumesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_sla_target_error_component import (
        ApiV1KubernetesVolumesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_slo_availability_error_component import (
        ApiV1KubernetesVolumesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_slo_target_error_component import (
        ApiV1KubernetesVolumesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_storage_class_error_component import (
        ApiV1KubernetesVolumesPartialUpdateStorageClassErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_target_availability_error_component import (
        ApiV1KubernetesVolumesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_partial_update_volume_mode_error_component import (
        ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesVolumesPartialUpdateValidationError")


@_attrs_define
class ApiV1KubernetesVolumesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateAnnotationsErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateArchivedErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateCriticalityErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateDebugModeErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateDisplayNameErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateK8SAppErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateK8SClusterErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateKindErrorComponent | ApiV1KubernetesVolumesPartialUpdateLabelsErrorComponent
            | ApiV1KubernetesVolumesPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateNameErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponent |
            ApiV1KubernetesVolumesPartialUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateProviderErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateProviderIdErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponent |
            ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateScopeErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateSlaTargetErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateSloTargetErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateStorageClassErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateAnnotationsErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateArchivedErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateCriticalityErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateDebugModeErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateDisplayNameErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateK8SAppErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateK8SClusterErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateKindErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateLabelsErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateNameErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponent
        | ApiV1KubernetesVolumesPartialUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateProviderErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateProviderIdErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponent
        | ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateScopeErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateSlaTargetErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateSloTargetErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateStorageClassErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_volumes_partial_update_access_modes_error_component import (
            ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_actual_availability_error_component import (
            ApiV1KubernetesVolumesPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_annotations_error_component import (
            ApiV1KubernetesVolumesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_archived_at_error_component import (
            ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_archived_error_component import (
            ApiV1KubernetesVolumesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_archived_reason_error_component import (
            ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_capacity_bytes_error_component import (
            ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_capacity_string_error_component import (
            ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_cloud_provider_volume_id_error_component import (
            ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_criticality_error_component import (
            ApiV1KubernetesVolumesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_csi_driver_error_component import (
            ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_debug_mode_error_component import (
            ApiV1KubernetesVolumesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesVolumesPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_display_name_error_component import (
            ApiV1KubernetesVolumesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_k8s_app_error_component import (
            ApiV1KubernetesVolumesPartialUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_k8s_cluster_error_component import (
            ApiV1KubernetesVolumesPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_kind_error_component import (
            ApiV1KubernetesVolumesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_labels_error_component import (
            ApiV1KubernetesVolumesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_managed_by_content_type_error_component import (
            ApiV1KubernetesVolumesPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_name_error_component import (
            ApiV1KubernetesVolumesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_node_affinity_error_component import (
            ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesVolumesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_phase_error_component import (
            ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_platform_service_error_component import (
            ApiV1KubernetesVolumesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_provider_error_component import (
            ApiV1KubernetesVolumesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_provider_id_error_component import (
            ApiV1KubernetesVolumesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_provider_object_id_error_component import (
            ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_provider_object_name_error_component import (
            ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_provider_reference_error_component import (
            ApiV1KubernetesVolumesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_pvc_name_error_component import (
            ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_pvc_namespace_error_component import (
            ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_reclaim_policy_error_component import (
            ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesVolumesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_scope_error_component import (
            ApiV1KubernetesVolumesPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_sla_availability_error_component import (
            ApiV1KubernetesVolumesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_sla_target_error_component import (
            ApiV1KubernetesVolumesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_slo_availability_error_component import (
            ApiV1KubernetesVolumesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_slo_target_error_component import (
            ApiV1KubernetesVolumesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_storage_class_error_component import (
            ApiV1KubernetesVolumesPartialUpdateStorageClassErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_target_availability_error_component import (
            ApiV1KubernetesVolumesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_volume_mode_error_component import (
            ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesPartialUpdateManagedByContentTypeErrorComponent):
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
        from ..models.api_v1_kubernetes_volumes_partial_update_access_modes_error_component import (
            ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_actual_availability_error_component import (
            ApiV1KubernetesVolumesPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_annotations_error_component import (
            ApiV1KubernetesVolumesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_archived_at_error_component import (
            ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_archived_error_component import (
            ApiV1KubernetesVolumesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_archived_reason_error_component import (
            ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_capacity_bytes_error_component import (
            ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_capacity_string_error_component import (
            ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_cloud_provider_volume_id_error_component import (
            ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_criticality_error_component import (
            ApiV1KubernetesVolumesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_csi_driver_error_component import (
            ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_debug_mode_error_component import (
            ApiV1KubernetesVolumesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesVolumesPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_display_name_error_component import (
            ApiV1KubernetesVolumesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_k8s_app_error_component import (
            ApiV1KubernetesVolumesPartialUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_k8s_cluster_error_component import (
            ApiV1KubernetesVolumesPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_kind_error_component import (
            ApiV1KubernetesVolumesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_labels_error_component import (
            ApiV1KubernetesVolumesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_managed_by_content_type_error_component import (
            ApiV1KubernetesVolumesPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_managed_by_object_id_error_component import (
            ApiV1KubernetesVolumesPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_name_error_component import (
            ApiV1KubernetesVolumesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_node_affinity_error_component import (
            ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesVolumesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_phase_error_component import (
            ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_platform_service_error_component import (
            ApiV1KubernetesVolumesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_provider_error_component import (
            ApiV1KubernetesVolumesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_provider_id_error_component import (
            ApiV1KubernetesVolumesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_provider_object_id_error_component import (
            ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_provider_object_name_error_component import (
            ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_provider_reference_error_component import (
            ApiV1KubernetesVolumesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_pvc_name_error_component import (
            ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_pvc_namespace_error_component import (
            ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_reclaim_policy_error_component import (
            ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesVolumesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_scope_error_component import (
            ApiV1KubernetesVolumesPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_sla_availability_error_component import (
            ApiV1KubernetesVolumesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_sla_target_error_component import (
            ApiV1KubernetesVolumesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_slo_availability_error_component import (
            ApiV1KubernetesVolumesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_slo_target_error_component import (
            ApiV1KubernetesVolumesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_storage_class_error_component import (
            ApiV1KubernetesVolumesPartialUpdateStorageClassErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_target_availability_error_component import (
            ApiV1KubernetesVolumesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_volumes_partial_update_volume_mode_error_component import (
            ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateAnnotationsErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateArchivedErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateCriticalityErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateDebugModeErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateDisplayNameErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateK8SAppErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateK8SClusterErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateKindErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateLabelsErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateNameErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponent
                | ApiV1KubernetesVolumesPartialUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateProviderErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateProviderIdErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponent
                | ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateScopeErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateSlaTargetErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateSloTargetErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateStorageClassErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_0 = (
                        ApiV1KubernetesVolumesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_1 = (
                        ApiV1KubernetesVolumesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_2 = (
                        ApiV1KubernetesVolumesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_3 = (
                        ApiV1KubernetesVolumesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_4 = (
                        ApiV1KubernetesVolumesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_5 = (
                        ApiV1KubernetesVolumesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_6 = (
                        ApiV1KubernetesVolumesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_7 = (
                        ApiV1KubernetesVolumesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_8 = (
                        ApiV1KubernetesVolumesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_9 = (
                        ApiV1KubernetesVolumesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_10 = (
                        ApiV1KubernetesVolumesPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_11 = (
                        ApiV1KubernetesVolumesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_12 = (
                        ApiV1KubernetesVolumesPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_13 = (
                        ApiV1KubernetesVolumesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_14 = (
                        ApiV1KubernetesVolumesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_15 = (
                        ApiV1KubernetesVolumesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_16 = (
                        ApiV1KubernetesVolumesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_17 = (
                        ApiV1KubernetesVolumesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_18 = (
                        ApiV1KubernetesVolumesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_19 = (
                        ApiV1KubernetesVolumesPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_20 = (
                        ApiV1KubernetesVolumesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_21 = (
                        ApiV1KubernetesVolumesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_22 = (
                        ApiV1KubernetesVolumesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_23 = (
                        ApiV1KubernetesVolumesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_24 = (
                        ApiV1KubernetesVolumesPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_25 = (
                        ApiV1KubernetesVolumesPartialUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_26 = (
                        ApiV1KubernetesVolumesPartialUpdateProviderObjectNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_27 = (
                        ApiV1KubernetesVolumesPartialUpdateProviderObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_28 = (
                        ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_29 = (
                        ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_30 = (
                        ApiV1KubernetesVolumesPartialUpdateStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_31 = (
                        ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_32 = (
                        ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_33 = (
                        ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_34 = (
                        ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_35 = (
                        ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_36 = (
                        ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_37 = (
                        ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_38 = (
                        ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_39 = (
                        ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_40 = (
                        ApiV1KubernetesVolumesPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_41 = (
                    ApiV1KubernetesVolumesPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_volumes_partial_update_error_type_41

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_volumes_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_volumes_partial_update_validation_error.additional_properties = d
        return api_v1_kubernetes_volumes_partial_update_validation_error

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
