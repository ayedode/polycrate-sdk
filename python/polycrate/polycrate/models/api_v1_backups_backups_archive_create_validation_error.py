from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_backups_backups_archive_create_annotations_error_component import (
        ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_archived_at_error_component import (
        ApiV1BackupsBackupsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_archived_error_component import (
        ApiV1BackupsBackupsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_archived_reason_error_component import (
        ApiV1BackupsBackupsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_completed_at_error_component import (
        ApiV1BackupsBackupsArchiveCreateCompletedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_criticality_error_component import (
        ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_debug_mode_error_component import (
        ApiV1BackupsBackupsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_display_name_error_component import (
        ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_expiration_error_component import (
        ApiV1BackupsBackupsArchiveCreateExpirationErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_items_backed_up_error_component import (
        ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_k8s_cluster_error_component import (
        ApiV1BackupsBackupsArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_kind_error_component import (
        ApiV1BackupsBackupsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_labels_error_component import (
        ApiV1BackupsBackupsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_metadata_error_component import (
        ApiV1BackupsBackupsArchiveCreateMetadataErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_name_error_component import (
        ApiV1BackupsBackupsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_non_field_errors_error_component import (
        ApiV1BackupsBackupsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_platform_service_error_component import (
        ApiV1BackupsBackupsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_provider_error_component import (
        ApiV1BackupsBackupsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_provider_id_error_component import (
        ApiV1BackupsBackupsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_provider_reference_error_component import (
        ApiV1BackupsBackupsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_reconciliation_enabled_error_component import (
        ApiV1BackupsBackupsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_retention_policy_error_component import (
        ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_schedule_error_component import (
        ApiV1BackupsBackupsArchiveCreateScheduleErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_size_bytes_error_component import (
        ApiV1BackupsBackupsArchiveCreateSizeBytesErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_sla_availability_error_component import (
        ApiV1BackupsBackupsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_sla_target_error_component import (
        ApiV1BackupsBackupsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_slo_availability_error_component import (
        ApiV1BackupsBackupsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_slo_target_error_component import (
        ApiV1BackupsBackupsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_source_namespace_error_component import (
        ApiV1BackupsBackupsArchiveCreateSourceNamespaceErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_started_at_error_component import (
        ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_status_error_component import (
        ApiV1BackupsBackupsArchiveCreateStatusErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_target_availability_error_component import (
        ApiV1BackupsBackupsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_archive_create_tolerations_error_component import (
        ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BackupsBackupsArchiveCreateValidationError")


@_attrs_define
class ApiV1BackupsBackupsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponent |
            ApiV1BackupsBackupsArchiveCreateArchivedAtErrorComponent |
            ApiV1BackupsBackupsArchiveCreateArchivedErrorComponent |
            ApiV1BackupsBackupsArchiveCreateArchivedReasonErrorComponent |
            ApiV1BackupsBackupsArchiveCreateCompletedAtErrorComponent |
            ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponent |
            ApiV1BackupsBackupsArchiveCreateDebugModeErrorComponent |
            ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponent |
            ApiV1BackupsBackupsArchiveCreateExpirationErrorComponent |
            ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponent |
            ApiV1BackupsBackupsArchiveCreateK8SClusterErrorComponent | ApiV1BackupsBackupsArchiveCreateKindErrorComponent |
            ApiV1BackupsBackupsArchiveCreateLabelsErrorComponent | ApiV1BackupsBackupsArchiveCreateMetadataErrorComponent |
            ApiV1BackupsBackupsArchiveCreateNameErrorComponent |
            ApiV1BackupsBackupsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1BackupsBackupsArchiveCreatePlatformServiceErrorComponent |
            ApiV1BackupsBackupsArchiveCreateProviderErrorComponent |
            ApiV1BackupsBackupsArchiveCreateProviderIdErrorComponent |
            ApiV1BackupsBackupsArchiveCreateProviderReferenceErrorComponent |
            ApiV1BackupsBackupsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponent |
            ApiV1BackupsBackupsArchiveCreateScheduleErrorComponent | ApiV1BackupsBackupsArchiveCreateSizeBytesErrorComponent
            | ApiV1BackupsBackupsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1BackupsBackupsArchiveCreateSlaTargetErrorComponent |
            ApiV1BackupsBackupsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1BackupsBackupsArchiveCreateSloTargetErrorComponent |
            ApiV1BackupsBackupsArchiveCreateSourceNamespaceErrorComponent |
            ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponent | ApiV1BackupsBackupsArchiveCreateStatusErrorComponent |
            ApiV1BackupsBackupsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponent
        | ApiV1BackupsBackupsArchiveCreateArchivedAtErrorComponent
        | ApiV1BackupsBackupsArchiveCreateArchivedErrorComponent
        | ApiV1BackupsBackupsArchiveCreateArchivedReasonErrorComponent
        | ApiV1BackupsBackupsArchiveCreateCompletedAtErrorComponent
        | ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponent
        | ApiV1BackupsBackupsArchiveCreateDebugModeErrorComponent
        | ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponent
        | ApiV1BackupsBackupsArchiveCreateExpirationErrorComponent
        | ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponent
        | ApiV1BackupsBackupsArchiveCreateK8SClusterErrorComponent
        | ApiV1BackupsBackupsArchiveCreateKindErrorComponent
        | ApiV1BackupsBackupsArchiveCreateLabelsErrorComponent
        | ApiV1BackupsBackupsArchiveCreateMetadataErrorComponent
        | ApiV1BackupsBackupsArchiveCreateNameErrorComponent
        | ApiV1BackupsBackupsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1BackupsBackupsArchiveCreatePlatformServiceErrorComponent
        | ApiV1BackupsBackupsArchiveCreateProviderErrorComponent
        | ApiV1BackupsBackupsArchiveCreateProviderIdErrorComponent
        | ApiV1BackupsBackupsArchiveCreateProviderReferenceErrorComponent
        | ApiV1BackupsBackupsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponent
        | ApiV1BackupsBackupsArchiveCreateScheduleErrorComponent
        | ApiV1BackupsBackupsArchiveCreateSizeBytesErrorComponent
        | ApiV1BackupsBackupsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1BackupsBackupsArchiveCreateSlaTargetErrorComponent
        | ApiV1BackupsBackupsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1BackupsBackupsArchiveCreateSloTargetErrorComponent
        | ApiV1BackupsBackupsArchiveCreateSourceNamespaceErrorComponent
        | ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponent
        | ApiV1BackupsBackupsArchiveCreateStatusErrorComponent
        | ApiV1BackupsBackupsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_backups_backups_archive_create_annotations_error_component import (
            ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_archived_at_error_component import (
            ApiV1BackupsBackupsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_archived_error_component import (
            ApiV1BackupsBackupsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_archived_reason_error_component import (
            ApiV1BackupsBackupsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_completed_at_error_component import (
            ApiV1BackupsBackupsArchiveCreateCompletedAtErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_criticality_error_component import (
            ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_debug_mode_error_component import (
            ApiV1BackupsBackupsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_display_name_error_component import (
            ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_expiration_error_component import (
            ApiV1BackupsBackupsArchiveCreateExpirationErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_items_backed_up_error_component import (
            ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_k8s_cluster_error_component import (
            ApiV1BackupsBackupsArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_kind_error_component import (
            ApiV1BackupsBackupsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_labels_error_component import (
            ApiV1BackupsBackupsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_name_error_component import (
            ApiV1BackupsBackupsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_non_field_errors_error_component import (
            ApiV1BackupsBackupsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_platform_service_error_component import (
            ApiV1BackupsBackupsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_provider_error_component import (
            ApiV1BackupsBackupsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_provider_id_error_component import (
            ApiV1BackupsBackupsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_provider_reference_error_component import (
            ApiV1BackupsBackupsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_retention_policy_error_component import (
            ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_schedule_error_component import (
            ApiV1BackupsBackupsArchiveCreateScheduleErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_size_bytes_error_component import (
            ApiV1BackupsBackupsArchiveCreateSizeBytesErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_sla_availability_error_component import (
            ApiV1BackupsBackupsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_sla_target_error_component import (
            ApiV1BackupsBackupsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_slo_availability_error_component import (
            ApiV1BackupsBackupsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_slo_target_error_component import (
            ApiV1BackupsBackupsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_source_namespace_error_component import (
            ApiV1BackupsBackupsArchiveCreateSourceNamespaceErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_started_at_error_component import (
            ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_status_error_component import (
            ApiV1BackupsBackupsArchiveCreateStatusErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_target_availability_error_component import (
            ApiV1BackupsBackupsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_tolerations_error_component import (
            ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateSourceNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateScheduleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateCompletedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateExpirationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateSizeBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponent):
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
        from ..models.api_v1_backups_backups_archive_create_annotations_error_component import (
            ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_archived_at_error_component import (
            ApiV1BackupsBackupsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_archived_error_component import (
            ApiV1BackupsBackupsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_archived_reason_error_component import (
            ApiV1BackupsBackupsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_completed_at_error_component import (
            ApiV1BackupsBackupsArchiveCreateCompletedAtErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_criticality_error_component import (
            ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_debug_mode_error_component import (
            ApiV1BackupsBackupsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_display_name_error_component import (
            ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_expiration_error_component import (
            ApiV1BackupsBackupsArchiveCreateExpirationErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_items_backed_up_error_component import (
            ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_k8s_cluster_error_component import (
            ApiV1BackupsBackupsArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_kind_error_component import (
            ApiV1BackupsBackupsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_labels_error_component import (
            ApiV1BackupsBackupsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_metadata_error_component import (
            ApiV1BackupsBackupsArchiveCreateMetadataErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_name_error_component import (
            ApiV1BackupsBackupsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_non_field_errors_error_component import (
            ApiV1BackupsBackupsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_platform_service_error_component import (
            ApiV1BackupsBackupsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_provider_error_component import (
            ApiV1BackupsBackupsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_provider_id_error_component import (
            ApiV1BackupsBackupsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_provider_reference_error_component import (
            ApiV1BackupsBackupsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_retention_policy_error_component import (
            ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_schedule_error_component import (
            ApiV1BackupsBackupsArchiveCreateScheduleErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_size_bytes_error_component import (
            ApiV1BackupsBackupsArchiveCreateSizeBytesErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_sla_availability_error_component import (
            ApiV1BackupsBackupsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_sla_target_error_component import (
            ApiV1BackupsBackupsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_slo_availability_error_component import (
            ApiV1BackupsBackupsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_slo_target_error_component import (
            ApiV1BackupsBackupsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_source_namespace_error_component import (
            ApiV1BackupsBackupsArchiveCreateSourceNamespaceErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_started_at_error_component import (
            ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_status_error_component import (
            ApiV1BackupsBackupsArchiveCreateStatusErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_target_availability_error_component import (
            ApiV1BackupsBackupsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backups_archive_create_tolerations_error_component import (
            ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponent
                | ApiV1BackupsBackupsArchiveCreateArchivedAtErrorComponent
                | ApiV1BackupsBackupsArchiveCreateArchivedErrorComponent
                | ApiV1BackupsBackupsArchiveCreateArchivedReasonErrorComponent
                | ApiV1BackupsBackupsArchiveCreateCompletedAtErrorComponent
                | ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponent
                | ApiV1BackupsBackupsArchiveCreateDebugModeErrorComponent
                | ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponent
                | ApiV1BackupsBackupsArchiveCreateExpirationErrorComponent
                | ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponent
                | ApiV1BackupsBackupsArchiveCreateK8SClusterErrorComponent
                | ApiV1BackupsBackupsArchiveCreateKindErrorComponent
                | ApiV1BackupsBackupsArchiveCreateLabelsErrorComponent
                | ApiV1BackupsBackupsArchiveCreateMetadataErrorComponent
                | ApiV1BackupsBackupsArchiveCreateNameErrorComponent
                | ApiV1BackupsBackupsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1BackupsBackupsArchiveCreatePlatformServiceErrorComponent
                | ApiV1BackupsBackupsArchiveCreateProviderErrorComponent
                | ApiV1BackupsBackupsArchiveCreateProviderIdErrorComponent
                | ApiV1BackupsBackupsArchiveCreateProviderReferenceErrorComponent
                | ApiV1BackupsBackupsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponent
                | ApiV1BackupsBackupsArchiveCreateScheduleErrorComponent
                | ApiV1BackupsBackupsArchiveCreateSizeBytesErrorComponent
                | ApiV1BackupsBackupsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1BackupsBackupsArchiveCreateSlaTargetErrorComponent
                | ApiV1BackupsBackupsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1BackupsBackupsArchiveCreateSloTargetErrorComponent
                | ApiV1BackupsBackupsArchiveCreateSourceNamespaceErrorComponent
                | ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponent
                | ApiV1BackupsBackupsArchiveCreateStatusErrorComponent
                | ApiV1BackupsBackupsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_0 = (
                        ApiV1BackupsBackupsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_1 = (
                        ApiV1BackupsBackupsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_2 = (
                        ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_3 = (
                        ApiV1BackupsBackupsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_4 = (
                        ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_5 = (
                        ApiV1BackupsBackupsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_6 = (
                        ApiV1BackupsBackupsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_7 = (
                        ApiV1BackupsBackupsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_8 = (
                        ApiV1BackupsBackupsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_9 = (
                        ApiV1BackupsBackupsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_10 = (
                        ApiV1BackupsBackupsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_11 = (
                        ApiV1BackupsBackupsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_12 = (
                        ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_13 = (
                        ApiV1BackupsBackupsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_14 = (
                        ApiV1BackupsBackupsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_15 = (
                        ApiV1BackupsBackupsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_16 = (
                        ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_17 = (
                        ApiV1BackupsBackupsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_18 = (
                        ApiV1BackupsBackupsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_19 = (
                        ApiV1BackupsBackupsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_20 = (
                        ApiV1BackupsBackupsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_21 = (
                        ApiV1BackupsBackupsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_22 = (
                        ApiV1BackupsBackupsArchiveCreateSourceNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_23 = (
                        ApiV1BackupsBackupsArchiveCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_24 = (
                        ApiV1BackupsBackupsArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_25 = (
                        ApiV1BackupsBackupsArchiveCreateScheduleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_26 = (
                        ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_27 = (
                        ApiV1BackupsBackupsArchiveCreateCompletedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_28 = (
                        ApiV1BackupsBackupsArchiveCreateExpirationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_29 = (
                        ApiV1BackupsBackupsArchiveCreateSizeBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_30 = (
                        ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_archive_create_error_type_31 = (
                        ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backups_archive_create_error_type_32 = (
                    ApiV1BackupsBackupsArchiveCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backups_archive_create_error_type_32

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_backups_backups_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_backups_backups_archive_create_validation_error.additional_properties = d
        return api_v1_backups_backups_archive_create_validation_error

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
