from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_volumes_create_access_modes_error_component import (
        ApiV1KubernetesVolumesCreateAccessModesErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_actual_availability_error_component import (
        ApiV1KubernetesVolumesCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_annotations_error_component import (
        ApiV1KubernetesVolumesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_archived_at_error_component import (
        ApiV1KubernetesVolumesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_archived_error_component import (
        ApiV1KubernetesVolumesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_archived_reason_error_component import (
        ApiV1KubernetesVolumesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_capacity_bytes_error_component import (
        ApiV1KubernetesVolumesCreateCapacityBytesErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_capacity_string_error_component import (
        ApiV1KubernetesVolumesCreateCapacityStringErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_cloud_provider_volume_id_error_component import (
        ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_criticality_error_component import (
        ApiV1KubernetesVolumesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_csi_driver_error_component import (
        ApiV1KubernetesVolumesCreateCsiDriverErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_debug_mode_error_component import (
        ApiV1KubernetesVolumesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_discovery_enabled_error_component import (
        ApiV1KubernetesVolumesCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_display_name_error_component import (
        ApiV1KubernetesVolumesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_k8s_app_error_component import (
        ApiV1KubernetesVolumesCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_k8s_cluster_error_component import (
        ApiV1KubernetesVolumesCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_kind_error_component import (
        ApiV1KubernetesVolumesCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_labels_error_component import (
        ApiV1KubernetesVolumesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_managed_by_content_type_error_component import (
        ApiV1KubernetesVolumesCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_managed_by_object_id_error_component import (
        ApiV1KubernetesVolumesCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_name_error_component import (
        ApiV1KubernetesVolumesCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_node_affinity_error_component import (
        ApiV1KubernetesVolumesCreateNodeAffinityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_non_field_errors_error_component import (
        ApiV1KubernetesVolumesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_phase_error_component import (
        ApiV1KubernetesVolumesCreatePhaseErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_platform_service_error_component import (
        ApiV1KubernetesVolumesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_provider_error_component import (
        ApiV1KubernetesVolumesCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_provider_id_error_component import (
        ApiV1KubernetesVolumesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_provider_object_id_error_component import (
        ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_provider_object_name_error_component import (
        ApiV1KubernetesVolumesCreateProviderObjectNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_provider_reference_error_component import (
        ApiV1KubernetesVolumesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_pvc_name_error_component import (
        ApiV1KubernetesVolumesCreatePvcNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_pvc_namespace_error_component import (
        ApiV1KubernetesVolumesCreatePvcNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_reclaim_policy_error_component import (
        ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesVolumesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_scope_error_component import (
        ApiV1KubernetesVolumesCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_sla_availability_error_component import (
        ApiV1KubernetesVolumesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_sla_target_error_component import (
        ApiV1KubernetesVolumesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_slo_availability_error_component import (
        ApiV1KubernetesVolumesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_slo_target_error_component import (
        ApiV1KubernetesVolumesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_storage_class_error_component import (
        ApiV1KubernetesVolumesCreateStorageClassErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_target_availability_error_component import (
        ApiV1KubernetesVolumesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_create_volume_mode_error_component import (
        ApiV1KubernetesVolumesCreateVolumeModeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesVolumesCreateValidationError")


@_attrs_define
class ApiV1KubernetesVolumesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesVolumesCreateAccessModesErrorComponent |
            ApiV1KubernetesVolumesCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesVolumesCreateAnnotationsErrorComponent | ApiV1KubernetesVolumesCreateArchivedAtErrorComponent |
            ApiV1KubernetesVolumesCreateArchivedErrorComponent | ApiV1KubernetesVolumesCreateArchivedReasonErrorComponent |
            ApiV1KubernetesVolumesCreateCapacityBytesErrorComponent |
            ApiV1KubernetesVolumesCreateCapacityStringErrorComponent |
            ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponent |
            ApiV1KubernetesVolumesCreateCriticalityErrorComponent | ApiV1KubernetesVolumesCreateCsiDriverErrorComponent |
            ApiV1KubernetesVolumesCreateDebugModeErrorComponent | ApiV1KubernetesVolumesCreateDiscoveryEnabledErrorComponent
            | ApiV1KubernetesVolumesCreateDisplayNameErrorComponent | ApiV1KubernetesVolumesCreateK8SAppErrorComponent |
            ApiV1KubernetesVolumesCreateK8SClusterErrorComponent | ApiV1KubernetesVolumesCreateKindErrorComponent |
            ApiV1KubernetesVolumesCreateLabelsErrorComponent |
            ApiV1KubernetesVolumesCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesVolumesCreateManagedByObjectIdErrorComponent | ApiV1KubernetesVolumesCreateNameErrorComponent |
            ApiV1KubernetesVolumesCreateNodeAffinityErrorComponent |
            ApiV1KubernetesVolumesCreateNonFieldErrorsErrorComponent | ApiV1KubernetesVolumesCreatePhaseErrorComponent |
            ApiV1KubernetesVolumesCreatePlatformServiceErrorComponent | ApiV1KubernetesVolumesCreateProviderErrorComponent |
            ApiV1KubernetesVolumesCreateProviderIdErrorComponent |
            ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponent |
            ApiV1KubernetesVolumesCreateProviderObjectNameErrorComponent |
            ApiV1KubernetesVolumesCreateProviderReferenceErrorComponent | ApiV1KubernetesVolumesCreatePvcNameErrorComponent
            | ApiV1KubernetesVolumesCreatePvcNamespaceErrorComponent |
            ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponent |
            ApiV1KubernetesVolumesCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesVolumesCreateScopeErrorComponent | ApiV1KubernetesVolumesCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesVolumesCreateSlaTargetErrorComponent | ApiV1KubernetesVolumesCreateSloAvailabilityErrorComponent
            | ApiV1KubernetesVolumesCreateSloTargetErrorComponent | ApiV1KubernetesVolumesCreateStorageClassErrorComponent |
            ApiV1KubernetesVolumesCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesVolumesCreateVolumeModeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesVolumesCreateAccessModesErrorComponent
        | ApiV1KubernetesVolumesCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesVolumesCreateAnnotationsErrorComponent
        | ApiV1KubernetesVolumesCreateArchivedAtErrorComponent
        | ApiV1KubernetesVolumesCreateArchivedErrorComponent
        | ApiV1KubernetesVolumesCreateArchivedReasonErrorComponent
        | ApiV1KubernetesVolumesCreateCapacityBytesErrorComponent
        | ApiV1KubernetesVolumesCreateCapacityStringErrorComponent
        | ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponent
        | ApiV1KubernetesVolumesCreateCriticalityErrorComponent
        | ApiV1KubernetesVolumesCreateCsiDriverErrorComponent
        | ApiV1KubernetesVolumesCreateDebugModeErrorComponent
        | ApiV1KubernetesVolumesCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesVolumesCreateDisplayNameErrorComponent
        | ApiV1KubernetesVolumesCreateK8SAppErrorComponent
        | ApiV1KubernetesVolumesCreateK8SClusterErrorComponent
        | ApiV1KubernetesVolumesCreateKindErrorComponent
        | ApiV1KubernetesVolumesCreateLabelsErrorComponent
        | ApiV1KubernetesVolumesCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesVolumesCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesVolumesCreateNameErrorComponent
        | ApiV1KubernetesVolumesCreateNodeAffinityErrorComponent
        | ApiV1KubernetesVolumesCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesVolumesCreatePhaseErrorComponent
        | ApiV1KubernetesVolumesCreatePlatformServiceErrorComponent
        | ApiV1KubernetesVolumesCreateProviderErrorComponent
        | ApiV1KubernetesVolumesCreateProviderIdErrorComponent
        | ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponent
        | ApiV1KubernetesVolumesCreateProviderObjectNameErrorComponent
        | ApiV1KubernetesVolumesCreateProviderReferenceErrorComponent
        | ApiV1KubernetesVolumesCreatePvcNameErrorComponent
        | ApiV1KubernetesVolumesCreatePvcNamespaceErrorComponent
        | ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponent
        | ApiV1KubernetesVolumesCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesVolumesCreateScopeErrorComponent
        | ApiV1KubernetesVolumesCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesVolumesCreateSlaTargetErrorComponent
        | ApiV1KubernetesVolumesCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesVolumesCreateSloTargetErrorComponent
        | ApiV1KubernetesVolumesCreateStorageClassErrorComponent
        | ApiV1KubernetesVolumesCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesVolumesCreateVolumeModeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_volumes_create_access_modes_error_component import (
            ApiV1KubernetesVolumesCreateAccessModesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_actual_availability_error_component import (
            ApiV1KubernetesVolumesCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_annotations_error_component import (
            ApiV1KubernetesVolumesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_archived_at_error_component import (
            ApiV1KubernetesVolumesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_archived_error_component import (
            ApiV1KubernetesVolumesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_archived_reason_error_component import (
            ApiV1KubernetesVolumesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_capacity_bytes_error_component import (
            ApiV1KubernetesVolumesCreateCapacityBytesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_capacity_string_error_component import (
            ApiV1KubernetesVolumesCreateCapacityStringErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_cloud_provider_volume_id_error_component import (
            ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_criticality_error_component import (
            ApiV1KubernetesVolumesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_csi_driver_error_component import (
            ApiV1KubernetesVolumesCreateCsiDriverErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_debug_mode_error_component import (
            ApiV1KubernetesVolumesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_discovery_enabled_error_component import (
            ApiV1KubernetesVolumesCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_display_name_error_component import (
            ApiV1KubernetesVolumesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_k8s_app_error_component import (
            ApiV1KubernetesVolumesCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_k8s_cluster_error_component import (
            ApiV1KubernetesVolumesCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_kind_error_component import (
            ApiV1KubernetesVolumesCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_labels_error_component import (
            ApiV1KubernetesVolumesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_managed_by_content_type_error_component import (
            ApiV1KubernetesVolumesCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_name_error_component import (
            ApiV1KubernetesVolumesCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_node_affinity_error_component import (
            ApiV1KubernetesVolumesCreateNodeAffinityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_non_field_errors_error_component import (
            ApiV1KubernetesVolumesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_phase_error_component import (
            ApiV1KubernetesVolumesCreatePhaseErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_platform_service_error_component import (
            ApiV1KubernetesVolumesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_provider_error_component import (
            ApiV1KubernetesVolumesCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_provider_id_error_component import (
            ApiV1KubernetesVolumesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_provider_object_id_error_component import (
            ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_provider_object_name_error_component import (
            ApiV1KubernetesVolumesCreateProviderObjectNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_provider_reference_error_component import (
            ApiV1KubernetesVolumesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_pvc_name_error_component import (
            ApiV1KubernetesVolumesCreatePvcNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_pvc_namespace_error_component import (
            ApiV1KubernetesVolumesCreatePvcNamespaceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_reclaim_policy_error_component import (
            ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesVolumesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_scope_error_component import (
            ApiV1KubernetesVolumesCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_sla_availability_error_component import (
            ApiV1KubernetesVolumesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_sla_target_error_component import (
            ApiV1KubernetesVolumesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_slo_availability_error_component import (
            ApiV1KubernetesVolumesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_slo_target_error_component import (
            ApiV1KubernetesVolumesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_storage_class_error_component import (
            ApiV1KubernetesVolumesCreateStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_target_availability_error_component import (
            ApiV1KubernetesVolumesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_volume_mode_error_component import (
            ApiV1KubernetesVolumesCreateVolumeModeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesVolumesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateProviderObjectNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateCsiDriverErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateCapacityBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateCapacityStringErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreatePhaseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateAccessModesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateVolumeModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreatePvcNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreatePvcNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateNodeAffinityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesCreateManagedByContentTypeErrorComponent):
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
        from ..models.api_v1_kubernetes_volumes_create_access_modes_error_component import (
            ApiV1KubernetesVolumesCreateAccessModesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_actual_availability_error_component import (
            ApiV1KubernetesVolumesCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_annotations_error_component import (
            ApiV1KubernetesVolumesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_archived_at_error_component import (
            ApiV1KubernetesVolumesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_archived_error_component import (
            ApiV1KubernetesVolumesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_archived_reason_error_component import (
            ApiV1KubernetesVolumesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_capacity_bytes_error_component import (
            ApiV1KubernetesVolumesCreateCapacityBytesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_capacity_string_error_component import (
            ApiV1KubernetesVolumesCreateCapacityStringErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_cloud_provider_volume_id_error_component import (
            ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_criticality_error_component import (
            ApiV1KubernetesVolumesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_csi_driver_error_component import (
            ApiV1KubernetesVolumesCreateCsiDriverErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_debug_mode_error_component import (
            ApiV1KubernetesVolumesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_discovery_enabled_error_component import (
            ApiV1KubernetesVolumesCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_display_name_error_component import (
            ApiV1KubernetesVolumesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_k8s_app_error_component import (
            ApiV1KubernetesVolumesCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_k8s_cluster_error_component import (
            ApiV1KubernetesVolumesCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_kind_error_component import (
            ApiV1KubernetesVolumesCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_labels_error_component import (
            ApiV1KubernetesVolumesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_managed_by_content_type_error_component import (
            ApiV1KubernetesVolumesCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_managed_by_object_id_error_component import (
            ApiV1KubernetesVolumesCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_name_error_component import (
            ApiV1KubernetesVolumesCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_node_affinity_error_component import (
            ApiV1KubernetesVolumesCreateNodeAffinityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_non_field_errors_error_component import (
            ApiV1KubernetesVolumesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_phase_error_component import (
            ApiV1KubernetesVolumesCreatePhaseErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_platform_service_error_component import (
            ApiV1KubernetesVolumesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_provider_error_component import (
            ApiV1KubernetesVolumesCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_provider_id_error_component import (
            ApiV1KubernetesVolumesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_provider_object_id_error_component import (
            ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_provider_object_name_error_component import (
            ApiV1KubernetesVolumesCreateProviderObjectNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_provider_reference_error_component import (
            ApiV1KubernetesVolumesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_pvc_name_error_component import (
            ApiV1KubernetesVolumesCreatePvcNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_pvc_namespace_error_component import (
            ApiV1KubernetesVolumesCreatePvcNamespaceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_reclaim_policy_error_component import (
            ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesVolumesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_scope_error_component import (
            ApiV1KubernetesVolumesCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_sla_availability_error_component import (
            ApiV1KubernetesVolumesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_sla_target_error_component import (
            ApiV1KubernetesVolumesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_slo_availability_error_component import (
            ApiV1KubernetesVolumesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_slo_target_error_component import (
            ApiV1KubernetesVolumesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_storage_class_error_component import (
            ApiV1KubernetesVolumesCreateStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_target_availability_error_component import (
            ApiV1KubernetesVolumesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_create_volume_mode_error_component import (
            ApiV1KubernetesVolumesCreateVolumeModeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesVolumesCreateAccessModesErrorComponent
                | ApiV1KubernetesVolumesCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesVolumesCreateAnnotationsErrorComponent
                | ApiV1KubernetesVolumesCreateArchivedAtErrorComponent
                | ApiV1KubernetesVolumesCreateArchivedErrorComponent
                | ApiV1KubernetesVolumesCreateArchivedReasonErrorComponent
                | ApiV1KubernetesVolumesCreateCapacityBytesErrorComponent
                | ApiV1KubernetesVolumesCreateCapacityStringErrorComponent
                | ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponent
                | ApiV1KubernetesVolumesCreateCriticalityErrorComponent
                | ApiV1KubernetesVolumesCreateCsiDriverErrorComponent
                | ApiV1KubernetesVolumesCreateDebugModeErrorComponent
                | ApiV1KubernetesVolumesCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesVolumesCreateDisplayNameErrorComponent
                | ApiV1KubernetesVolumesCreateK8SAppErrorComponent
                | ApiV1KubernetesVolumesCreateK8SClusterErrorComponent
                | ApiV1KubernetesVolumesCreateKindErrorComponent
                | ApiV1KubernetesVolumesCreateLabelsErrorComponent
                | ApiV1KubernetesVolumesCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesVolumesCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesVolumesCreateNameErrorComponent
                | ApiV1KubernetesVolumesCreateNodeAffinityErrorComponent
                | ApiV1KubernetesVolumesCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesVolumesCreatePhaseErrorComponent
                | ApiV1KubernetesVolumesCreatePlatformServiceErrorComponent
                | ApiV1KubernetesVolumesCreateProviderErrorComponent
                | ApiV1KubernetesVolumesCreateProviderIdErrorComponent
                | ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponent
                | ApiV1KubernetesVolumesCreateProviderObjectNameErrorComponent
                | ApiV1KubernetesVolumesCreateProviderReferenceErrorComponent
                | ApiV1KubernetesVolumesCreatePvcNameErrorComponent
                | ApiV1KubernetesVolumesCreatePvcNamespaceErrorComponent
                | ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponent
                | ApiV1KubernetesVolumesCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesVolumesCreateScopeErrorComponent
                | ApiV1KubernetesVolumesCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesVolumesCreateSlaTargetErrorComponent
                | ApiV1KubernetesVolumesCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesVolumesCreateSloTargetErrorComponent
                | ApiV1KubernetesVolumesCreateStorageClassErrorComponent
                | ApiV1KubernetesVolumesCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesVolumesCreateVolumeModeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_0 = (
                        ApiV1KubernetesVolumesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_1 = (
                        ApiV1KubernetesVolumesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_2 = (
                        ApiV1KubernetesVolumesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_3 = (
                        ApiV1KubernetesVolumesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_4 = (
                        ApiV1KubernetesVolumesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_5 = (
                        ApiV1KubernetesVolumesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_6 = (
                        ApiV1KubernetesVolumesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_7 = (
                        ApiV1KubernetesVolumesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_8 = (
                        ApiV1KubernetesVolumesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_9 = (
                        ApiV1KubernetesVolumesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_10 = (
                        ApiV1KubernetesVolumesCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_11 = (
                        ApiV1KubernetesVolumesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_12 = (
                        ApiV1KubernetesVolumesCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_13 = (
                        ApiV1KubernetesVolumesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_14 = (
                        ApiV1KubernetesVolumesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_15 = (
                        ApiV1KubernetesVolumesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_16 = (
                        ApiV1KubernetesVolumesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_17 = (
                        ApiV1KubernetesVolumesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_18 = (
                        ApiV1KubernetesVolumesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_19 = (
                        ApiV1KubernetesVolumesCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_20 = (
                        ApiV1KubernetesVolumesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_21 = (
                        ApiV1KubernetesVolumesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_22 = (
                        ApiV1KubernetesVolumesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_23 = (
                        ApiV1KubernetesVolumesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_24 = (
                        ApiV1KubernetesVolumesCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_25 = (
                        ApiV1KubernetesVolumesCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_26 = (
                        ApiV1KubernetesVolumesCreateProviderObjectNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_27 = (
                        ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_28 = (
                        ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_29 = (
                        ApiV1KubernetesVolumesCreateCsiDriverErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_30 = (
                        ApiV1KubernetesVolumesCreateStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_31 = (
                        ApiV1KubernetesVolumesCreateCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_32 = (
                        ApiV1KubernetesVolumesCreateCapacityStringErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_33 = (
                        ApiV1KubernetesVolumesCreatePhaseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_34 = (
                        ApiV1KubernetesVolumesCreateAccessModesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_35 = (
                        ApiV1KubernetesVolumesCreateVolumeModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_36 = (
                        ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_37 = (
                        ApiV1KubernetesVolumesCreatePvcNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_38 = (
                        ApiV1KubernetesVolumesCreatePvcNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_39 = (
                        ApiV1KubernetesVolumesCreateNodeAffinityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_create_error_type_40 = (
                        ApiV1KubernetesVolumesCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_volumes_create_error_type_41 = (
                    ApiV1KubernetesVolumesCreateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_volumes_create_error_type_41

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_volumes_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_volumes_create_validation_error.additional_properties = d
        return api_v1_kubernetes_volumes_create_validation_error

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
