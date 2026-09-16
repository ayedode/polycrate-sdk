from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_backups_backups_partial_update_annotations_error_component import (
        ApiV1BackupsBackupsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_archived_at_error_component import (
        ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_archived_error_component import (
        ApiV1BackupsBackupsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_archived_reason_error_component import (
        ApiV1BackupsBackupsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_completed_at_error_component import (
        ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_criticality_error_component import (
        ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_debug_mode_error_component import (
        ApiV1BackupsBackupsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_display_name_error_component import (
        ApiV1BackupsBackupsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_expiration_error_component import (
        ApiV1BackupsBackupsPartialUpdateExpirationErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_items_backed_up_error_component import (
        ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_k8s_cluster_error_component import (
        ApiV1BackupsBackupsPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_kind_error_component import (
        ApiV1BackupsBackupsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_labels_error_component import (
        ApiV1BackupsBackupsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_metadata_error_component import (
        ApiV1BackupsBackupsPartialUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_name_error_component import (
        ApiV1BackupsBackupsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_non_field_errors_error_component import (
        ApiV1BackupsBackupsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_platform_service_error_component import (
        ApiV1BackupsBackupsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_provider_error_component import (
        ApiV1BackupsBackupsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_provider_id_error_component import (
        ApiV1BackupsBackupsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_provider_reference_error_component import (
        ApiV1BackupsBackupsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_reconciliation_enabled_error_component import (
        ApiV1BackupsBackupsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_retention_policy_error_component import (
        ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_schedule_error_component import (
        ApiV1BackupsBackupsPartialUpdateScheduleErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_size_bytes_error_component import (
        ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_sla_availability_error_component import (
        ApiV1BackupsBackupsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_sla_target_error_component import (
        ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_slo_availability_error_component import (
        ApiV1BackupsBackupsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_slo_target_error_component import (
        ApiV1BackupsBackupsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_source_namespace_error_component import (
        ApiV1BackupsBackupsPartialUpdateSourceNamespaceErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_started_at_error_component import (
        ApiV1BackupsBackupsPartialUpdateStartedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_status_error_component import (
        ApiV1BackupsBackupsPartialUpdateStatusErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_target_availability_error_component import (
        ApiV1BackupsBackupsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_partial_update_tolerations_error_component import (
        ApiV1BackupsBackupsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BackupsBackupsPartialUpdateValidationError")


@_attrs_define
class ApiV1BackupsBackupsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BackupsBackupsPartialUpdateAnnotationsErrorComponent |
            ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponent |
            ApiV1BackupsBackupsPartialUpdateArchivedErrorComponent |
            ApiV1BackupsBackupsPartialUpdateArchivedReasonErrorComponent |
            ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponent |
            ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponent |
            ApiV1BackupsBackupsPartialUpdateDebugModeErrorComponent |
            ApiV1BackupsBackupsPartialUpdateDisplayNameErrorComponent |
            ApiV1BackupsBackupsPartialUpdateExpirationErrorComponent |
            ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponent |
            ApiV1BackupsBackupsPartialUpdateK8SClusterErrorComponent | ApiV1BackupsBackupsPartialUpdateKindErrorComponent |
            ApiV1BackupsBackupsPartialUpdateLabelsErrorComponent | ApiV1BackupsBackupsPartialUpdateMetadataErrorComponent |
            ApiV1BackupsBackupsPartialUpdateNameErrorComponent |
            ApiV1BackupsBackupsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1BackupsBackupsPartialUpdatePlatformServiceErrorComponent |
            ApiV1BackupsBackupsPartialUpdateProviderErrorComponent |
            ApiV1BackupsBackupsPartialUpdateProviderIdErrorComponent |
            ApiV1BackupsBackupsPartialUpdateProviderReferenceErrorComponent |
            ApiV1BackupsBackupsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponent |
            ApiV1BackupsBackupsPartialUpdateScheduleErrorComponent | ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponent
            | ApiV1BackupsBackupsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponent |
            ApiV1BackupsBackupsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1BackupsBackupsPartialUpdateSloTargetErrorComponent |
            ApiV1BackupsBackupsPartialUpdateSourceNamespaceErrorComponent |
            ApiV1BackupsBackupsPartialUpdateStartedAtErrorComponent | ApiV1BackupsBackupsPartialUpdateStatusErrorComponent |
            ApiV1BackupsBackupsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1BackupsBackupsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BackupsBackupsPartialUpdateAnnotationsErrorComponent
        | ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponent
        | ApiV1BackupsBackupsPartialUpdateArchivedErrorComponent
        | ApiV1BackupsBackupsPartialUpdateArchivedReasonErrorComponent
        | ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponent
        | ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponent
        | ApiV1BackupsBackupsPartialUpdateDebugModeErrorComponent
        | ApiV1BackupsBackupsPartialUpdateDisplayNameErrorComponent
        | ApiV1BackupsBackupsPartialUpdateExpirationErrorComponent
        | ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponent
        | ApiV1BackupsBackupsPartialUpdateK8SClusterErrorComponent
        | ApiV1BackupsBackupsPartialUpdateKindErrorComponent
        | ApiV1BackupsBackupsPartialUpdateLabelsErrorComponent
        | ApiV1BackupsBackupsPartialUpdateMetadataErrorComponent
        | ApiV1BackupsBackupsPartialUpdateNameErrorComponent
        | ApiV1BackupsBackupsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1BackupsBackupsPartialUpdatePlatformServiceErrorComponent
        | ApiV1BackupsBackupsPartialUpdateProviderErrorComponent
        | ApiV1BackupsBackupsPartialUpdateProviderIdErrorComponent
        | ApiV1BackupsBackupsPartialUpdateProviderReferenceErrorComponent
        | ApiV1BackupsBackupsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponent
        | ApiV1BackupsBackupsPartialUpdateScheduleErrorComponent
        | ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponent
        | ApiV1BackupsBackupsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponent
        | ApiV1BackupsBackupsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1BackupsBackupsPartialUpdateSloTargetErrorComponent
        | ApiV1BackupsBackupsPartialUpdateSourceNamespaceErrorComponent
        | ApiV1BackupsBackupsPartialUpdateStartedAtErrorComponent
        | ApiV1BackupsBackupsPartialUpdateStatusErrorComponent
        | ApiV1BackupsBackupsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1BackupsBackupsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_backups_backups_partial_update_annotations_error_component import (
            ApiV1BackupsBackupsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_archived_at_error_component import (
            ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_archived_error_component import (
            ApiV1BackupsBackupsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_archived_reason_error_component import (
            ApiV1BackupsBackupsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_completed_at_error_component import (
            ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_criticality_error_component import (
            ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_debug_mode_error_component import (
            ApiV1BackupsBackupsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_display_name_error_component import (
            ApiV1BackupsBackupsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_expiration_error_component import (
            ApiV1BackupsBackupsPartialUpdateExpirationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_items_backed_up_error_component import (
            ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_k8s_cluster_error_component import (
            ApiV1BackupsBackupsPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_kind_error_component import (
            ApiV1BackupsBackupsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_labels_error_component import (
            ApiV1BackupsBackupsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_name_error_component import (
            ApiV1BackupsBackupsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_non_field_errors_error_component import (
            ApiV1BackupsBackupsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_platform_service_error_component import (
            ApiV1BackupsBackupsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_provider_error_component import (
            ApiV1BackupsBackupsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_provider_id_error_component import (
            ApiV1BackupsBackupsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_provider_reference_error_component import (
            ApiV1BackupsBackupsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_retention_policy_error_component import (
            ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_schedule_error_component import (
            ApiV1BackupsBackupsPartialUpdateScheduleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_size_bytes_error_component import (
            ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_sla_availability_error_component import (
            ApiV1BackupsBackupsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_sla_target_error_component import (
            ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_slo_availability_error_component import (
            ApiV1BackupsBackupsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_slo_target_error_component import (
            ApiV1BackupsBackupsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_source_namespace_error_component import (
            ApiV1BackupsBackupsPartialUpdateSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_started_at_error_component import (
            ApiV1BackupsBackupsPartialUpdateStartedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_status_error_component import (
            ApiV1BackupsBackupsPartialUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_target_availability_error_component import (
            ApiV1BackupsBackupsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_tolerations_error_component import (
            ApiV1BackupsBackupsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateSourceNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateScheduleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateStartedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateExpirationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponent):
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
        from ..models.api_v1_backups_backups_partial_update_annotations_error_component import (
            ApiV1BackupsBackupsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_archived_at_error_component import (
            ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_archived_error_component import (
            ApiV1BackupsBackupsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_archived_reason_error_component import (
            ApiV1BackupsBackupsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_completed_at_error_component import (
            ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_criticality_error_component import (
            ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_debug_mode_error_component import (
            ApiV1BackupsBackupsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_display_name_error_component import (
            ApiV1BackupsBackupsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_expiration_error_component import (
            ApiV1BackupsBackupsPartialUpdateExpirationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_items_backed_up_error_component import (
            ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_k8s_cluster_error_component import (
            ApiV1BackupsBackupsPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_kind_error_component import (
            ApiV1BackupsBackupsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_labels_error_component import (
            ApiV1BackupsBackupsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_metadata_error_component import (
            ApiV1BackupsBackupsPartialUpdateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_name_error_component import (
            ApiV1BackupsBackupsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_non_field_errors_error_component import (
            ApiV1BackupsBackupsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_platform_service_error_component import (
            ApiV1BackupsBackupsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_provider_error_component import (
            ApiV1BackupsBackupsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_provider_id_error_component import (
            ApiV1BackupsBackupsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_provider_reference_error_component import (
            ApiV1BackupsBackupsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_retention_policy_error_component import (
            ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_schedule_error_component import (
            ApiV1BackupsBackupsPartialUpdateScheduleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_size_bytes_error_component import (
            ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_sla_availability_error_component import (
            ApiV1BackupsBackupsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_sla_target_error_component import (
            ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_slo_availability_error_component import (
            ApiV1BackupsBackupsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_slo_target_error_component import (
            ApiV1BackupsBackupsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_source_namespace_error_component import (
            ApiV1BackupsBackupsPartialUpdateSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_started_at_error_component import (
            ApiV1BackupsBackupsPartialUpdateStartedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_status_error_component import (
            ApiV1BackupsBackupsPartialUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_target_availability_error_component import (
            ApiV1BackupsBackupsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_partial_update_tolerations_error_component import (
            ApiV1BackupsBackupsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BackupsBackupsPartialUpdateAnnotationsErrorComponent
                | ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponent
                | ApiV1BackupsBackupsPartialUpdateArchivedErrorComponent
                | ApiV1BackupsBackupsPartialUpdateArchivedReasonErrorComponent
                | ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponent
                | ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponent
                | ApiV1BackupsBackupsPartialUpdateDebugModeErrorComponent
                | ApiV1BackupsBackupsPartialUpdateDisplayNameErrorComponent
                | ApiV1BackupsBackupsPartialUpdateExpirationErrorComponent
                | ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponent
                | ApiV1BackupsBackupsPartialUpdateK8SClusterErrorComponent
                | ApiV1BackupsBackupsPartialUpdateKindErrorComponent
                | ApiV1BackupsBackupsPartialUpdateLabelsErrorComponent
                | ApiV1BackupsBackupsPartialUpdateMetadataErrorComponent
                | ApiV1BackupsBackupsPartialUpdateNameErrorComponent
                | ApiV1BackupsBackupsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1BackupsBackupsPartialUpdatePlatformServiceErrorComponent
                | ApiV1BackupsBackupsPartialUpdateProviderErrorComponent
                | ApiV1BackupsBackupsPartialUpdateProviderIdErrorComponent
                | ApiV1BackupsBackupsPartialUpdateProviderReferenceErrorComponent
                | ApiV1BackupsBackupsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponent
                | ApiV1BackupsBackupsPartialUpdateScheduleErrorComponent
                | ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponent
                | ApiV1BackupsBackupsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponent
                | ApiV1BackupsBackupsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1BackupsBackupsPartialUpdateSloTargetErrorComponent
                | ApiV1BackupsBackupsPartialUpdateSourceNamespaceErrorComponent
                | ApiV1BackupsBackupsPartialUpdateStartedAtErrorComponent
                | ApiV1BackupsBackupsPartialUpdateStatusErrorComponent
                | ApiV1BackupsBackupsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1BackupsBackupsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_0 = (
                        ApiV1BackupsBackupsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_1 = (
                        ApiV1BackupsBackupsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_2 = (
                        ApiV1BackupsBackupsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_3 = (
                        ApiV1BackupsBackupsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_4 = (
                        ApiV1BackupsBackupsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_5 = (
                        ApiV1BackupsBackupsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_6 = (
                        ApiV1BackupsBackupsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_7 = (
                        ApiV1BackupsBackupsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_8 = (
                        ApiV1BackupsBackupsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_9 = (
                        ApiV1BackupsBackupsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_10 = (
                        ApiV1BackupsBackupsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_11 = (
                        ApiV1BackupsBackupsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_12 = (
                        ApiV1BackupsBackupsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_13 = (
                        ApiV1BackupsBackupsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_14 = (
                        ApiV1BackupsBackupsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_15 = (
                        ApiV1BackupsBackupsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_16 = (
                        ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_17 = (
                        ApiV1BackupsBackupsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_18 = (
                        ApiV1BackupsBackupsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_19 = (
                        ApiV1BackupsBackupsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_20 = (
                        ApiV1BackupsBackupsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_21 = (
                        ApiV1BackupsBackupsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_22 = (
                        ApiV1BackupsBackupsPartialUpdateSourceNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_23 = (
                        ApiV1BackupsBackupsPartialUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_24 = (
                        ApiV1BackupsBackupsPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_25 = (
                        ApiV1BackupsBackupsPartialUpdateScheduleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_26 = (
                        ApiV1BackupsBackupsPartialUpdateStartedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_27 = (
                        ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_28 = (
                        ApiV1BackupsBackupsPartialUpdateExpirationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_29 = (
                        ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_30 = (
                        ApiV1BackupsBackupsPartialUpdateItemsBackedUpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_partial_update_error_type_31 = (
                        ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backups_partial_update_error_type_32 = (
                    ApiV1BackupsBackupsPartialUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backups_partial_update_error_type_32

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_backups_backups_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_backups_backups_partial_update_validation_error.additional_properties = d
        return api_v1_backups_backups_partial_update_validation_error

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
