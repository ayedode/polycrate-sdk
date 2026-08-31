from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_volumes_archive_create_access_modes_error_component import (
        ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_actual_availability_error_component import (
        ApiV1KubernetesVolumesArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_annotations_error_component import (
        ApiV1KubernetesVolumesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_archived_at_error_component import (
        ApiV1KubernetesVolumesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_archived_error_component import (
        ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_archived_reason_error_component import (
        ApiV1KubernetesVolumesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_capacity_bytes_error_component import (
        ApiV1KubernetesVolumesArchiveCreateCapacityBytesErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_capacity_string_error_component import (
        ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_cloud_provider_volume_id_error_component import (
        ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_criticality_error_component import (
        ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_csi_driver_error_component import (
        ApiV1KubernetesVolumesArchiveCreateCsiDriverErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_debug_mode_error_component import (
        ApiV1KubernetesVolumesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_discovery_enabled_error_component import (
        ApiV1KubernetesVolumesArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_display_name_error_component import (
        ApiV1KubernetesVolumesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_k8s_app_error_component import (
        ApiV1KubernetesVolumesArchiveCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_k8s_cluster_error_component import (
        ApiV1KubernetesVolumesArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_kind_error_component import (
        ApiV1KubernetesVolumesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_labels_error_component import (
        ApiV1KubernetesVolumesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_managed_by_content_type_error_component import (
        ApiV1KubernetesVolumesArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_managed_by_object_id_error_component import (
        ApiV1KubernetesVolumesArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_name_error_component import (
        ApiV1KubernetesVolumesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_node_affinity_error_component import (
        ApiV1KubernetesVolumesArchiveCreateNodeAffinityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_non_field_errors_error_component import (
        ApiV1KubernetesVolumesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_phase_error_component import (
        ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_platform_service_error_component import (
        ApiV1KubernetesVolumesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_provider_error_component import (
        ApiV1KubernetesVolumesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_provider_id_error_component import (
        ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_provider_object_id_error_component import (
        ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_provider_object_name_error_component import (
        ApiV1KubernetesVolumesArchiveCreateProviderObjectNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_provider_reference_error_component import (
        ApiV1KubernetesVolumesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_pvc_name_error_component import (
        ApiV1KubernetesVolumesArchiveCreatePvcNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_pvc_namespace_error_component import (
        ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_reclaim_policy_error_component import (
        ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesVolumesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_scope_error_component import (
        ApiV1KubernetesVolumesArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_sla_availability_error_component import (
        ApiV1KubernetesVolumesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_sla_target_error_component import (
        ApiV1KubernetesVolumesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_slo_availability_error_component import (
        ApiV1KubernetesVolumesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_slo_target_error_component import (
        ApiV1KubernetesVolumesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_storage_class_error_component import (
        ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_target_availability_error_component import (
        ApiV1KubernetesVolumesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_volumes_archive_create_volume_mode_error_component import (
        ApiV1KubernetesVolumesArchiveCreateVolumeModeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesVolumesArchiveCreateValidationError")


@_attrs_define
class ApiV1KubernetesVolumesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateAnnotationsErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateArchivedAtErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateArchivedReasonErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateCapacityBytesErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateCsiDriverErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateDebugModeErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateDisplayNameErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateK8SAppErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateK8SClusterErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateKindErrorComponent | ApiV1KubernetesVolumesArchiveCreateLabelsErrorComponent
            | ApiV1KubernetesVolumesArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateNameErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateNodeAffinityErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponent |
            ApiV1KubernetesVolumesArchiveCreatePlatformServiceErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateProviderErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateProviderObjectNameErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateProviderReferenceErrorComponent |
            ApiV1KubernetesVolumesArchiveCreatePvcNameErrorComponent |
            ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateScopeErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateSlaTargetErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateSloTargetErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesVolumesArchiveCreateVolumeModeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateAnnotationsErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateArchivedAtErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateArchivedReasonErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateCapacityBytesErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateCsiDriverErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateDebugModeErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateDisplayNameErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateK8SAppErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateK8SClusterErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateKindErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateLabelsErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateNameErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateNodeAffinityErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponent
        | ApiV1KubernetesVolumesArchiveCreatePlatformServiceErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateProviderErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateProviderObjectNameErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateProviderReferenceErrorComponent
        | ApiV1KubernetesVolumesArchiveCreatePvcNameErrorComponent
        | ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateScopeErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateSlaTargetErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateSloTargetErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesVolumesArchiveCreateVolumeModeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_volumes_archive_create_access_modes_error_component import (
            ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_actual_availability_error_component import (
            ApiV1KubernetesVolumesArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_annotations_error_component import (
            ApiV1KubernetesVolumesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_archived_at_error_component import (
            ApiV1KubernetesVolumesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_archived_error_component import (
            ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_archived_reason_error_component import (
            ApiV1KubernetesVolumesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_capacity_bytes_error_component import (
            ApiV1KubernetesVolumesArchiveCreateCapacityBytesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_capacity_string_error_component import (
            ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_cloud_provider_volume_id_error_component import (
            ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_criticality_error_component import (
            ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_csi_driver_error_component import (
            ApiV1KubernetesVolumesArchiveCreateCsiDriverErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_debug_mode_error_component import (
            ApiV1KubernetesVolumesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesVolumesArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_display_name_error_component import (
            ApiV1KubernetesVolumesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_k8s_app_error_component import (
            ApiV1KubernetesVolumesArchiveCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_k8s_cluster_error_component import (
            ApiV1KubernetesVolumesArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_kind_error_component import (
            ApiV1KubernetesVolumesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_labels_error_component import (
            ApiV1KubernetesVolumesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_managed_by_content_type_error_component import (
            ApiV1KubernetesVolumesArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_name_error_component import (
            ApiV1KubernetesVolumesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_node_affinity_error_component import (
            ApiV1KubernetesVolumesArchiveCreateNodeAffinityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesVolumesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_phase_error_component import (
            ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_platform_service_error_component import (
            ApiV1KubernetesVolumesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_provider_error_component import (
            ApiV1KubernetesVolumesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_provider_id_error_component import (
            ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_provider_object_id_error_component import (
            ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_provider_object_name_error_component import (
            ApiV1KubernetesVolumesArchiveCreateProviderObjectNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_provider_reference_error_component import (
            ApiV1KubernetesVolumesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_pvc_name_error_component import (
            ApiV1KubernetesVolumesArchiveCreatePvcNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_pvc_namespace_error_component import (
            ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_reclaim_policy_error_component import (
            ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesVolumesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_scope_error_component import (
            ApiV1KubernetesVolumesArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_sla_availability_error_component import (
            ApiV1KubernetesVolumesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_sla_target_error_component import (
            ApiV1KubernetesVolumesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_slo_availability_error_component import (
            ApiV1KubernetesVolumesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_slo_target_error_component import (
            ApiV1KubernetesVolumesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_storage_class_error_component import (
            ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_target_availability_error_component import (
            ApiV1KubernetesVolumesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_volume_mode_error_component import (
            ApiV1KubernetesVolumesArchiveCreateVolumeModeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateProviderObjectNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateCsiDriverErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateCapacityBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateVolumeModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreatePvcNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateNodeAffinityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesVolumesArchiveCreateManagedByContentTypeErrorComponent):
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
        from ..models.api_v1_kubernetes_volumes_archive_create_access_modes_error_component import (
            ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_actual_availability_error_component import (
            ApiV1KubernetesVolumesArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_annotations_error_component import (
            ApiV1KubernetesVolumesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_archived_at_error_component import (
            ApiV1KubernetesVolumesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_archived_error_component import (
            ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_archived_reason_error_component import (
            ApiV1KubernetesVolumesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_capacity_bytes_error_component import (
            ApiV1KubernetesVolumesArchiveCreateCapacityBytesErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_capacity_string_error_component import (
            ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_cloud_provider_volume_id_error_component import (
            ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_criticality_error_component import (
            ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_csi_driver_error_component import (
            ApiV1KubernetesVolumesArchiveCreateCsiDriverErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_debug_mode_error_component import (
            ApiV1KubernetesVolumesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesVolumesArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_display_name_error_component import (
            ApiV1KubernetesVolumesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_k8s_app_error_component import (
            ApiV1KubernetesVolumesArchiveCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_k8s_cluster_error_component import (
            ApiV1KubernetesVolumesArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_kind_error_component import (
            ApiV1KubernetesVolumesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_labels_error_component import (
            ApiV1KubernetesVolumesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_managed_by_content_type_error_component import (
            ApiV1KubernetesVolumesArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_managed_by_object_id_error_component import (
            ApiV1KubernetesVolumesArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_name_error_component import (
            ApiV1KubernetesVolumesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_node_affinity_error_component import (
            ApiV1KubernetesVolumesArchiveCreateNodeAffinityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesVolumesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_phase_error_component import (
            ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_platform_service_error_component import (
            ApiV1KubernetesVolumesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_provider_error_component import (
            ApiV1KubernetesVolumesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_provider_id_error_component import (
            ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_provider_object_id_error_component import (
            ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_provider_object_name_error_component import (
            ApiV1KubernetesVolumesArchiveCreateProviderObjectNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_provider_reference_error_component import (
            ApiV1KubernetesVolumesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_pvc_name_error_component import (
            ApiV1KubernetesVolumesArchiveCreatePvcNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_pvc_namespace_error_component import (
            ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_reclaim_policy_error_component import (
            ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesVolumesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_scope_error_component import (
            ApiV1KubernetesVolumesArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_sla_availability_error_component import (
            ApiV1KubernetesVolumesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_sla_target_error_component import (
            ApiV1KubernetesVolumesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_slo_availability_error_component import (
            ApiV1KubernetesVolumesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_slo_target_error_component import (
            ApiV1KubernetesVolumesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_storage_class_error_component import (
            ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_target_availability_error_component import (
            ApiV1KubernetesVolumesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_volumes_archive_create_volume_mode_error_component import (
            ApiV1KubernetesVolumesArchiveCreateVolumeModeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateAnnotationsErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateArchivedAtErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateArchivedReasonErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateCapacityBytesErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateCsiDriverErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateDebugModeErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateDisplayNameErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateK8SAppErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateK8SClusterErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateKindErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateLabelsErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateNameErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateNodeAffinityErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponent
                | ApiV1KubernetesVolumesArchiveCreatePlatformServiceErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateProviderErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateProviderObjectNameErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateProviderReferenceErrorComponent
                | ApiV1KubernetesVolumesArchiveCreatePvcNameErrorComponent
                | ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateScopeErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateSlaTargetErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateSloTargetErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesVolumesArchiveCreateVolumeModeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_0 = (
                        ApiV1KubernetesVolumesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_1 = (
                        ApiV1KubernetesVolumesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_2 = (
                        ApiV1KubernetesVolumesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_3 = (
                        ApiV1KubernetesVolumesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_4 = (
                        ApiV1KubernetesVolumesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_5 = (
                        ApiV1KubernetesVolumesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_6 = (
                        ApiV1KubernetesVolumesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_7 = (
                        ApiV1KubernetesVolumesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_8 = (
                        ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_9 = (
                        ApiV1KubernetesVolumesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_10 = (
                        ApiV1KubernetesVolumesArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_11 = (
                        ApiV1KubernetesVolumesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_12 = (
                        ApiV1KubernetesVolumesArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_13 = (
                        ApiV1KubernetesVolumesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_14 = (
                        ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_15 = (
                        ApiV1KubernetesVolumesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_16 = (
                        ApiV1KubernetesVolumesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_17 = (
                        ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_18 = (
                        ApiV1KubernetesVolumesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_19 = (
                        ApiV1KubernetesVolumesArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_20 = (
                        ApiV1KubernetesVolumesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_21 = (
                        ApiV1KubernetesVolumesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_22 = (
                        ApiV1KubernetesVolumesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_23 = (
                        ApiV1KubernetesVolumesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_24 = (
                        ApiV1KubernetesVolumesArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_25 = (
                        ApiV1KubernetesVolumesArchiveCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_26 = (
                        ApiV1KubernetesVolumesArchiveCreateProviderObjectNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_27 = (
                        ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_28 = (
                        ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_29 = (
                        ApiV1KubernetesVolumesArchiveCreateCsiDriverErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_30 = (
                        ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_31 = (
                        ApiV1KubernetesVolumesArchiveCreateCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_32 = (
                        ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_33 = (
                        ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_34 = (
                        ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_35 = (
                        ApiV1KubernetesVolumesArchiveCreateVolumeModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_36 = (
                        ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_37 = (
                        ApiV1KubernetesVolumesArchiveCreatePvcNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_38 = (
                        ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_39 = (
                        ApiV1KubernetesVolumesArchiveCreateNodeAffinityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_40 = (
                        ApiV1KubernetesVolumesArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_41 = (
                    ApiV1KubernetesVolumesArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_volumes_archive_create_error_type_41

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_volumes_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_volumes_archive_create_validation_error.additional_properties = d
        return api_v1_kubernetes_volumes_archive_create_validation_error

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
