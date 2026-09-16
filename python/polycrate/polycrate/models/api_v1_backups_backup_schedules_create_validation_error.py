from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_backups_backup_schedules_create_annotations_error_component import (
        ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_archived_at_error_component import (
        ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_archived_error_component import (
        ApiV1BackupsBackupSchedulesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_archived_reason_error_component import (
        ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_criticality_error_component import (
        ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_debug_mode_error_component import (
        ApiV1BackupsBackupSchedulesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_display_name_error_component import (
        ApiV1BackupsBackupSchedulesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_k8s_cluster_error_component import (
        ApiV1BackupsBackupSchedulesCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_kind_error_component import (
        ApiV1BackupsBackupSchedulesCreateKindErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_labels_error_component import (
        ApiV1BackupsBackupSchedulesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_last_backup_at_error_component import (
        ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_metadata_error_component import (
        ApiV1BackupsBackupSchedulesCreateMetadataErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_name_error_component import (
        ApiV1BackupsBackupSchedulesCreateNameErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_non_field_errors_error_component import (
        ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_paused_error_component import (
        ApiV1BackupsBackupSchedulesCreatePausedErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_platform_service_error_component import (
        ApiV1BackupsBackupSchedulesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_provider_error_component import (
        ApiV1BackupsBackupSchedulesCreateProviderErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_provider_id_error_component import (
        ApiV1BackupsBackupSchedulesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_provider_reference_error_component import (
        ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_reconciliation_enabled_error_component import (
        ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_retention_policy_error_component import (
        ApiV1BackupsBackupSchedulesCreateRetentionPolicyErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_schedule_cron_error_component import (
        ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_sla_availability_error_component import (
        ApiV1BackupsBackupSchedulesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_sla_target_error_component import (
        ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_slo_availability_error_component import (
        ApiV1BackupsBackupSchedulesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_slo_target_error_component import (
        ApiV1BackupsBackupSchedulesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_source_namespace_error_component import (
        ApiV1BackupsBackupSchedulesCreateSourceNamespaceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_status_error_component import (
        ApiV1BackupsBackupSchedulesCreateStatusErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_target_availability_error_component import (
        ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_tolerations_error_component import (
        ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_create_total_backups_error_component import (
        ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BackupsBackupSchedulesCreateValidationError")


@_attrs_define
class ApiV1BackupsBackupSchedulesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponent |
            ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponent |
            ApiV1BackupsBackupSchedulesCreateArchivedErrorComponent |
            ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponent |
            ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponent |
            ApiV1BackupsBackupSchedulesCreateDebugModeErrorComponent |
            ApiV1BackupsBackupSchedulesCreateDisplayNameErrorComponent |
            ApiV1BackupsBackupSchedulesCreateK8SClusterErrorComponent | ApiV1BackupsBackupSchedulesCreateKindErrorComponent
            | ApiV1BackupsBackupSchedulesCreateLabelsErrorComponent |
            ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponent |
            ApiV1BackupsBackupSchedulesCreateMetadataErrorComponent | ApiV1BackupsBackupSchedulesCreateNameErrorComponent |
            ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponent |
            ApiV1BackupsBackupSchedulesCreatePausedErrorComponent |
            ApiV1BackupsBackupSchedulesCreatePlatformServiceErrorComponent |
            ApiV1BackupsBackupSchedulesCreateProviderErrorComponent |
            ApiV1BackupsBackupSchedulesCreateProviderIdErrorComponent |
            ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponent |
            ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponent |
            ApiV1BackupsBackupSchedulesCreateRetentionPolicyErrorComponent |
            ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponent |
            ApiV1BackupsBackupSchedulesCreateSlaAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponent |
            ApiV1BackupsBackupSchedulesCreateSloAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesCreateSloTargetErrorComponent |
            ApiV1BackupsBackupSchedulesCreateSourceNamespaceErrorComponent |
            ApiV1BackupsBackupSchedulesCreateStatusErrorComponent |
            ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponent |
            ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponent
        | ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponent
        | ApiV1BackupsBackupSchedulesCreateArchivedErrorComponent
        | ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponent
        | ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponent
        | ApiV1BackupsBackupSchedulesCreateDebugModeErrorComponent
        | ApiV1BackupsBackupSchedulesCreateDisplayNameErrorComponent
        | ApiV1BackupsBackupSchedulesCreateK8SClusterErrorComponent
        | ApiV1BackupsBackupSchedulesCreateKindErrorComponent
        | ApiV1BackupsBackupSchedulesCreateLabelsErrorComponent
        | ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponent
        | ApiV1BackupsBackupSchedulesCreateMetadataErrorComponent
        | ApiV1BackupsBackupSchedulesCreateNameErrorComponent
        | ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponent
        | ApiV1BackupsBackupSchedulesCreatePausedErrorComponent
        | ApiV1BackupsBackupSchedulesCreatePlatformServiceErrorComponent
        | ApiV1BackupsBackupSchedulesCreateProviderErrorComponent
        | ApiV1BackupsBackupSchedulesCreateProviderIdErrorComponent
        | ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponent
        | ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponent
        | ApiV1BackupsBackupSchedulesCreateRetentionPolicyErrorComponent
        | ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponent
        | ApiV1BackupsBackupSchedulesCreateSlaAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponent
        | ApiV1BackupsBackupSchedulesCreateSloAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesCreateSloTargetErrorComponent
        | ApiV1BackupsBackupSchedulesCreateSourceNamespaceErrorComponent
        | ApiV1BackupsBackupSchedulesCreateStatusErrorComponent
        | ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponent
        | ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_backups_backup_schedules_create_annotations_error_component import (
            ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_archived_at_error_component import (
            ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_archived_error_component import (
            ApiV1BackupsBackupSchedulesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_archived_reason_error_component import (
            ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_criticality_error_component import (
            ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_debug_mode_error_component import (
            ApiV1BackupsBackupSchedulesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_display_name_error_component import (
            ApiV1BackupsBackupSchedulesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_k8s_cluster_error_component import (
            ApiV1BackupsBackupSchedulesCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_kind_error_component import (
            ApiV1BackupsBackupSchedulesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_labels_error_component import (
            ApiV1BackupsBackupSchedulesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_last_backup_at_error_component import (
            ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_name_error_component import (
            ApiV1BackupsBackupSchedulesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_non_field_errors_error_component import (
            ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_paused_error_component import (
            ApiV1BackupsBackupSchedulesCreatePausedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_platform_service_error_component import (
            ApiV1BackupsBackupSchedulesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_provider_error_component import (
            ApiV1BackupsBackupSchedulesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_provider_id_error_component import (
            ApiV1BackupsBackupSchedulesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_provider_reference_error_component import (
            ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_retention_policy_error_component import (
            ApiV1BackupsBackupSchedulesCreateRetentionPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_schedule_cron_error_component import (
            ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_sla_availability_error_component import (
            ApiV1BackupsBackupSchedulesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_sla_target_error_component import (
            ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_slo_availability_error_component import (
            ApiV1BackupsBackupSchedulesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_slo_target_error_component import (
            ApiV1BackupsBackupSchedulesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_source_namespace_error_component import (
            ApiV1BackupsBackupSchedulesCreateSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_status_error_component import (
            ApiV1BackupsBackupSchedulesCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_target_availability_error_component import (
            ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_tolerations_error_component import (
            ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_total_backups_error_component import (
            ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateSourceNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreatePausedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateRetentionPolicyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponent):
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
        from ..models.api_v1_backups_backup_schedules_create_annotations_error_component import (
            ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_archived_at_error_component import (
            ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_archived_error_component import (
            ApiV1BackupsBackupSchedulesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_archived_reason_error_component import (
            ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_criticality_error_component import (
            ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_debug_mode_error_component import (
            ApiV1BackupsBackupSchedulesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_display_name_error_component import (
            ApiV1BackupsBackupSchedulesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_k8s_cluster_error_component import (
            ApiV1BackupsBackupSchedulesCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_kind_error_component import (
            ApiV1BackupsBackupSchedulesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_labels_error_component import (
            ApiV1BackupsBackupSchedulesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_last_backup_at_error_component import (
            ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_metadata_error_component import (
            ApiV1BackupsBackupSchedulesCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_name_error_component import (
            ApiV1BackupsBackupSchedulesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_non_field_errors_error_component import (
            ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_paused_error_component import (
            ApiV1BackupsBackupSchedulesCreatePausedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_platform_service_error_component import (
            ApiV1BackupsBackupSchedulesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_provider_error_component import (
            ApiV1BackupsBackupSchedulesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_provider_id_error_component import (
            ApiV1BackupsBackupSchedulesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_provider_reference_error_component import (
            ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_retention_policy_error_component import (
            ApiV1BackupsBackupSchedulesCreateRetentionPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_schedule_cron_error_component import (
            ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_sla_availability_error_component import (
            ApiV1BackupsBackupSchedulesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_sla_target_error_component import (
            ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_slo_availability_error_component import (
            ApiV1BackupsBackupSchedulesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_slo_target_error_component import (
            ApiV1BackupsBackupSchedulesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_source_namespace_error_component import (
            ApiV1BackupsBackupSchedulesCreateSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_status_error_component import (
            ApiV1BackupsBackupSchedulesCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_target_availability_error_component import (
            ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_tolerations_error_component import (
            ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_create_total_backups_error_component import (
            ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponent
                | ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponent
                | ApiV1BackupsBackupSchedulesCreateArchivedErrorComponent
                | ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponent
                | ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponent
                | ApiV1BackupsBackupSchedulesCreateDebugModeErrorComponent
                | ApiV1BackupsBackupSchedulesCreateDisplayNameErrorComponent
                | ApiV1BackupsBackupSchedulesCreateK8SClusterErrorComponent
                | ApiV1BackupsBackupSchedulesCreateKindErrorComponent
                | ApiV1BackupsBackupSchedulesCreateLabelsErrorComponent
                | ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponent
                | ApiV1BackupsBackupSchedulesCreateMetadataErrorComponent
                | ApiV1BackupsBackupSchedulesCreateNameErrorComponent
                | ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponent
                | ApiV1BackupsBackupSchedulesCreatePausedErrorComponent
                | ApiV1BackupsBackupSchedulesCreatePlatformServiceErrorComponent
                | ApiV1BackupsBackupSchedulesCreateProviderErrorComponent
                | ApiV1BackupsBackupSchedulesCreateProviderIdErrorComponent
                | ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponent
                | ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponent
                | ApiV1BackupsBackupSchedulesCreateRetentionPolicyErrorComponent
                | ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponent
                | ApiV1BackupsBackupSchedulesCreateSlaAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponent
                | ApiV1BackupsBackupSchedulesCreateSloAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesCreateSloTargetErrorComponent
                | ApiV1BackupsBackupSchedulesCreateSourceNamespaceErrorComponent
                | ApiV1BackupsBackupSchedulesCreateStatusErrorComponent
                | ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponent
                | ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_0 = (
                        ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_1 = (
                        ApiV1BackupsBackupSchedulesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_2 = (
                        ApiV1BackupsBackupSchedulesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_3 = (
                        ApiV1BackupsBackupSchedulesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_4 = (
                        ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_5 = (
                        ApiV1BackupsBackupSchedulesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_6 = (
                        ApiV1BackupsBackupSchedulesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_7 = (
                        ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_8 = (
                        ApiV1BackupsBackupSchedulesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_9 = (
                        ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_10 = (
                        ApiV1BackupsBackupSchedulesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_11 = (
                        ApiV1BackupsBackupSchedulesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_12 = (
                        ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_13 = (
                        ApiV1BackupsBackupSchedulesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_14 = (
                        ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_15 = (
                        ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_16 = (
                        ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_17 = (
                        ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_18 = (
                        ApiV1BackupsBackupSchedulesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_19 = (
                        ApiV1BackupsBackupSchedulesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_20 = (
                        ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_21 = (
                        ApiV1BackupsBackupSchedulesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_22 = (
                        ApiV1BackupsBackupSchedulesCreateSourceNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_23 = (
                        ApiV1BackupsBackupSchedulesCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_24 = (
                        ApiV1BackupsBackupSchedulesCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_25 = (
                        ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_26 = (
                        ApiV1BackupsBackupSchedulesCreatePausedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_27 = (
                        ApiV1BackupsBackupSchedulesCreateRetentionPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_28 = (
                        ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_create_error_type_29 = (
                        ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backup_schedules_create_error_type_30 = (
                    ApiV1BackupsBackupSchedulesCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backup_schedules_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_backups_backup_schedules_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_backups_backup_schedules_create_validation_error.additional_properties = d
        return api_v1_backups_backup_schedules_create_validation_error

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
