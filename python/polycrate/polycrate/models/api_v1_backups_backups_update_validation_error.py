from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_backups_backups_update_annotations_error_component import (
        ApiV1BackupsBackupsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_archived_at_error_component import (
        ApiV1BackupsBackupsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_archived_error_component import (
        ApiV1BackupsBackupsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_archived_reason_error_component import (
        ApiV1BackupsBackupsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_completed_at_error_component import (
        ApiV1BackupsBackupsUpdateCompletedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_criticality_error_component import (
        ApiV1BackupsBackupsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_debug_mode_error_component import (
        ApiV1BackupsBackupsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_display_name_error_component import (
        ApiV1BackupsBackupsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_expiration_error_component import (
        ApiV1BackupsBackupsUpdateExpirationErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_items_backed_up_error_component import (
        ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_k8s_cluster_error_component import (
        ApiV1BackupsBackupsUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_kind_error_component import ApiV1BackupsBackupsUpdateKindErrorComponent
    from ..models.api_v1_backups_backups_update_labels_error_component import (
        ApiV1BackupsBackupsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_metadata_error_component import (
        ApiV1BackupsBackupsUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_name_error_component import ApiV1BackupsBackupsUpdateNameErrorComponent
    from ..models.api_v1_backups_backups_update_non_field_errors_error_component import (
        ApiV1BackupsBackupsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_platform_service_error_component import (
        ApiV1BackupsBackupsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_provider_error_component import (
        ApiV1BackupsBackupsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_provider_id_error_component import (
        ApiV1BackupsBackupsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_provider_reference_error_component import (
        ApiV1BackupsBackupsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_reconciliation_enabled_error_component import (
        ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_retention_policy_error_component import (
        ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_schedule_error_component import (
        ApiV1BackupsBackupsUpdateScheduleErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_size_bytes_error_component import (
        ApiV1BackupsBackupsUpdateSizeBytesErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_sla_availability_error_component import (
        ApiV1BackupsBackupsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_sla_target_error_component import (
        ApiV1BackupsBackupsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_slo_availability_error_component import (
        ApiV1BackupsBackupsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_slo_target_error_component import (
        ApiV1BackupsBackupsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_source_namespace_error_component import (
        ApiV1BackupsBackupsUpdateSourceNamespaceErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_started_at_error_component import (
        ApiV1BackupsBackupsUpdateStartedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_status_error_component import (
        ApiV1BackupsBackupsUpdateStatusErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_target_availability_error_component import (
        ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_update_tolerations_error_component import (
        ApiV1BackupsBackupsUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BackupsBackupsUpdateValidationError")


@_attrs_define
class ApiV1BackupsBackupsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BackupsBackupsUpdateAnnotationsErrorComponent |
            ApiV1BackupsBackupsUpdateArchivedAtErrorComponent | ApiV1BackupsBackupsUpdateArchivedErrorComponent |
            ApiV1BackupsBackupsUpdateArchivedReasonErrorComponent | ApiV1BackupsBackupsUpdateCompletedAtErrorComponent |
            ApiV1BackupsBackupsUpdateCriticalityErrorComponent | ApiV1BackupsBackupsUpdateDebugModeErrorComponent |
            ApiV1BackupsBackupsUpdateDisplayNameErrorComponent | ApiV1BackupsBackupsUpdateExpirationErrorComponent |
            ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponent | ApiV1BackupsBackupsUpdateK8SClusterErrorComponent |
            ApiV1BackupsBackupsUpdateKindErrorComponent | ApiV1BackupsBackupsUpdateLabelsErrorComponent |
            ApiV1BackupsBackupsUpdateMetadataErrorComponent | ApiV1BackupsBackupsUpdateNameErrorComponent |
            ApiV1BackupsBackupsUpdateNonFieldErrorsErrorComponent | ApiV1BackupsBackupsUpdatePlatformServiceErrorComponent |
            ApiV1BackupsBackupsUpdateProviderErrorComponent | ApiV1BackupsBackupsUpdateProviderIdErrorComponent |
            ApiV1BackupsBackupsUpdateProviderReferenceErrorComponent |
            ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponent |
            ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponent | ApiV1BackupsBackupsUpdateScheduleErrorComponent |
            ApiV1BackupsBackupsUpdateSizeBytesErrorComponent | ApiV1BackupsBackupsUpdateSlaAvailabilityErrorComponent |
            ApiV1BackupsBackupsUpdateSlaTargetErrorComponent | ApiV1BackupsBackupsUpdateSloAvailabilityErrorComponent |
            ApiV1BackupsBackupsUpdateSloTargetErrorComponent | ApiV1BackupsBackupsUpdateSourceNamespaceErrorComponent |
            ApiV1BackupsBackupsUpdateStartedAtErrorComponent | ApiV1BackupsBackupsUpdateStatusErrorComponent |
            ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponent |
            ApiV1BackupsBackupsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BackupsBackupsUpdateAnnotationsErrorComponent
        | ApiV1BackupsBackupsUpdateArchivedAtErrorComponent
        | ApiV1BackupsBackupsUpdateArchivedErrorComponent
        | ApiV1BackupsBackupsUpdateArchivedReasonErrorComponent
        | ApiV1BackupsBackupsUpdateCompletedAtErrorComponent
        | ApiV1BackupsBackupsUpdateCriticalityErrorComponent
        | ApiV1BackupsBackupsUpdateDebugModeErrorComponent
        | ApiV1BackupsBackupsUpdateDisplayNameErrorComponent
        | ApiV1BackupsBackupsUpdateExpirationErrorComponent
        | ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponent
        | ApiV1BackupsBackupsUpdateK8SClusterErrorComponent
        | ApiV1BackupsBackupsUpdateKindErrorComponent
        | ApiV1BackupsBackupsUpdateLabelsErrorComponent
        | ApiV1BackupsBackupsUpdateMetadataErrorComponent
        | ApiV1BackupsBackupsUpdateNameErrorComponent
        | ApiV1BackupsBackupsUpdateNonFieldErrorsErrorComponent
        | ApiV1BackupsBackupsUpdatePlatformServiceErrorComponent
        | ApiV1BackupsBackupsUpdateProviderErrorComponent
        | ApiV1BackupsBackupsUpdateProviderIdErrorComponent
        | ApiV1BackupsBackupsUpdateProviderReferenceErrorComponent
        | ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponent
        | ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponent
        | ApiV1BackupsBackupsUpdateScheduleErrorComponent
        | ApiV1BackupsBackupsUpdateSizeBytesErrorComponent
        | ApiV1BackupsBackupsUpdateSlaAvailabilityErrorComponent
        | ApiV1BackupsBackupsUpdateSlaTargetErrorComponent
        | ApiV1BackupsBackupsUpdateSloAvailabilityErrorComponent
        | ApiV1BackupsBackupsUpdateSloTargetErrorComponent
        | ApiV1BackupsBackupsUpdateSourceNamespaceErrorComponent
        | ApiV1BackupsBackupsUpdateStartedAtErrorComponent
        | ApiV1BackupsBackupsUpdateStatusErrorComponent
        | ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponent
        | ApiV1BackupsBackupsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_backups_backups_update_annotations_error_component import (
            ApiV1BackupsBackupsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_archived_at_error_component import (
            ApiV1BackupsBackupsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_archived_error_component import (
            ApiV1BackupsBackupsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_archived_reason_error_component import (
            ApiV1BackupsBackupsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_completed_at_error_component import (
            ApiV1BackupsBackupsUpdateCompletedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_criticality_error_component import (
            ApiV1BackupsBackupsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_debug_mode_error_component import (
            ApiV1BackupsBackupsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_display_name_error_component import (
            ApiV1BackupsBackupsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_expiration_error_component import (
            ApiV1BackupsBackupsUpdateExpirationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_items_backed_up_error_component import (
            ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_k8s_cluster_error_component import (
            ApiV1BackupsBackupsUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_kind_error_component import (
            ApiV1BackupsBackupsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_labels_error_component import (
            ApiV1BackupsBackupsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_name_error_component import (
            ApiV1BackupsBackupsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_non_field_errors_error_component import (
            ApiV1BackupsBackupsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_platform_service_error_component import (
            ApiV1BackupsBackupsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_provider_error_component import (
            ApiV1BackupsBackupsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_provider_id_error_component import (
            ApiV1BackupsBackupsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_provider_reference_error_component import (
            ApiV1BackupsBackupsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_retention_policy_error_component import (
            ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_schedule_error_component import (
            ApiV1BackupsBackupsUpdateScheduleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_size_bytes_error_component import (
            ApiV1BackupsBackupsUpdateSizeBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_sla_availability_error_component import (
            ApiV1BackupsBackupsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_sla_target_error_component import (
            ApiV1BackupsBackupsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_slo_availability_error_component import (
            ApiV1BackupsBackupsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_slo_target_error_component import (
            ApiV1BackupsBackupsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_source_namespace_error_component import (
            ApiV1BackupsBackupsUpdateSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_started_at_error_component import (
            ApiV1BackupsBackupsUpdateStartedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_status_error_component import (
            ApiV1BackupsBackupsUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_target_availability_error_component import (
            ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_tolerations_error_component import (
            ApiV1BackupsBackupsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BackupsBackupsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateSourceNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateScheduleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateStartedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateCompletedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateExpirationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateSizeBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponent):
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
        from ..models.api_v1_backups_backups_update_annotations_error_component import (
            ApiV1BackupsBackupsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_archived_at_error_component import (
            ApiV1BackupsBackupsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_archived_error_component import (
            ApiV1BackupsBackupsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_archived_reason_error_component import (
            ApiV1BackupsBackupsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_completed_at_error_component import (
            ApiV1BackupsBackupsUpdateCompletedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_criticality_error_component import (
            ApiV1BackupsBackupsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_debug_mode_error_component import (
            ApiV1BackupsBackupsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_display_name_error_component import (
            ApiV1BackupsBackupsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_expiration_error_component import (
            ApiV1BackupsBackupsUpdateExpirationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_items_backed_up_error_component import (
            ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_k8s_cluster_error_component import (
            ApiV1BackupsBackupsUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_kind_error_component import (
            ApiV1BackupsBackupsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_labels_error_component import (
            ApiV1BackupsBackupsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_metadata_error_component import (
            ApiV1BackupsBackupsUpdateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_name_error_component import (
            ApiV1BackupsBackupsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_non_field_errors_error_component import (
            ApiV1BackupsBackupsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_platform_service_error_component import (
            ApiV1BackupsBackupsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_provider_error_component import (
            ApiV1BackupsBackupsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_provider_id_error_component import (
            ApiV1BackupsBackupsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_provider_reference_error_component import (
            ApiV1BackupsBackupsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_retention_policy_error_component import (
            ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_schedule_error_component import (
            ApiV1BackupsBackupsUpdateScheduleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_size_bytes_error_component import (
            ApiV1BackupsBackupsUpdateSizeBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_sla_availability_error_component import (
            ApiV1BackupsBackupsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_sla_target_error_component import (
            ApiV1BackupsBackupsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_slo_availability_error_component import (
            ApiV1BackupsBackupsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_slo_target_error_component import (
            ApiV1BackupsBackupsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_source_namespace_error_component import (
            ApiV1BackupsBackupsUpdateSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_started_at_error_component import (
            ApiV1BackupsBackupsUpdateStartedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_status_error_component import (
            ApiV1BackupsBackupsUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_target_availability_error_component import (
            ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_update_tolerations_error_component import (
            ApiV1BackupsBackupsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BackupsBackupsUpdateAnnotationsErrorComponent
                | ApiV1BackupsBackupsUpdateArchivedAtErrorComponent
                | ApiV1BackupsBackupsUpdateArchivedErrorComponent
                | ApiV1BackupsBackupsUpdateArchivedReasonErrorComponent
                | ApiV1BackupsBackupsUpdateCompletedAtErrorComponent
                | ApiV1BackupsBackupsUpdateCriticalityErrorComponent
                | ApiV1BackupsBackupsUpdateDebugModeErrorComponent
                | ApiV1BackupsBackupsUpdateDisplayNameErrorComponent
                | ApiV1BackupsBackupsUpdateExpirationErrorComponent
                | ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponent
                | ApiV1BackupsBackupsUpdateK8SClusterErrorComponent
                | ApiV1BackupsBackupsUpdateKindErrorComponent
                | ApiV1BackupsBackupsUpdateLabelsErrorComponent
                | ApiV1BackupsBackupsUpdateMetadataErrorComponent
                | ApiV1BackupsBackupsUpdateNameErrorComponent
                | ApiV1BackupsBackupsUpdateNonFieldErrorsErrorComponent
                | ApiV1BackupsBackupsUpdatePlatformServiceErrorComponent
                | ApiV1BackupsBackupsUpdateProviderErrorComponent
                | ApiV1BackupsBackupsUpdateProviderIdErrorComponent
                | ApiV1BackupsBackupsUpdateProviderReferenceErrorComponent
                | ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponent
                | ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponent
                | ApiV1BackupsBackupsUpdateScheduleErrorComponent
                | ApiV1BackupsBackupsUpdateSizeBytesErrorComponent
                | ApiV1BackupsBackupsUpdateSlaAvailabilityErrorComponent
                | ApiV1BackupsBackupsUpdateSlaTargetErrorComponent
                | ApiV1BackupsBackupsUpdateSloAvailabilityErrorComponent
                | ApiV1BackupsBackupsUpdateSloTargetErrorComponent
                | ApiV1BackupsBackupsUpdateSourceNamespaceErrorComponent
                | ApiV1BackupsBackupsUpdateStartedAtErrorComponent
                | ApiV1BackupsBackupsUpdateStatusErrorComponent
                | ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponent
                | ApiV1BackupsBackupsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_0 = (
                        ApiV1BackupsBackupsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_1 = (
                        ApiV1BackupsBackupsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_2 = (
                        ApiV1BackupsBackupsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_3 = (
                        ApiV1BackupsBackupsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_4 = (
                        ApiV1BackupsBackupsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_5 = (
                        ApiV1BackupsBackupsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_6 = (
                        ApiV1BackupsBackupsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_7 = (
                        ApiV1BackupsBackupsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_8 = (
                        ApiV1BackupsBackupsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_9 = (
                        ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_10 = (
                        ApiV1BackupsBackupsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_11 = (
                        ApiV1BackupsBackupsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_12 = (
                        ApiV1BackupsBackupsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_13 = (
                        ApiV1BackupsBackupsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_14 = (
                        ApiV1BackupsBackupsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_15 = (
                        ApiV1BackupsBackupsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_16 = (
                        ApiV1BackupsBackupsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_17 = (
                        ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_18 = (
                        ApiV1BackupsBackupsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_19 = (
                        ApiV1BackupsBackupsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_20 = (
                        ApiV1BackupsBackupsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_21 = (
                        ApiV1BackupsBackupsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_22 = (
                        ApiV1BackupsBackupsUpdateSourceNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_23 = (
                        ApiV1BackupsBackupsUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_24 = (
                        ApiV1BackupsBackupsUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_25 = (
                        ApiV1BackupsBackupsUpdateScheduleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_26 = (
                        ApiV1BackupsBackupsUpdateStartedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_27 = (
                        ApiV1BackupsBackupsUpdateCompletedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_28 = (
                        ApiV1BackupsBackupsUpdateExpirationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_29 = (
                        ApiV1BackupsBackupsUpdateSizeBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_30 = (
                        ApiV1BackupsBackupsUpdateItemsBackedUpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_update_error_type_31 = (
                        ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backups_update_error_type_32 = (
                    ApiV1BackupsBackupsUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backups_update_error_type_32

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_backups_backups_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_backups_backups_update_validation_error.additional_properties = d
        return api_v1_backups_backups_update_validation_error

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
