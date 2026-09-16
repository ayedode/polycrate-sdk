from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_backups_backups_create_annotations_error_component import (
        ApiV1BackupsBackupsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_archived_at_error_component import (
        ApiV1BackupsBackupsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_archived_error_component import (
        ApiV1BackupsBackupsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_archived_reason_error_component import (
        ApiV1BackupsBackupsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_completed_at_error_component import (
        ApiV1BackupsBackupsCreateCompletedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_criticality_error_component import (
        ApiV1BackupsBackupsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_debug_mode_error_component import (
        ApiV1BackupsBackupsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_display_name_error_component import (
        ApiV1BackupsBackupsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_expiration_error_component import (
        ApiV1BackupsBackupsCreateExpirationErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_items_backed_up_error_component import (
        ApiV1BackupsBackupsCreateItemsBackedUpErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_k8s_cluster_error_component import (
        ApiV1BackupsBackupsCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_kind_error_component import ApiV1BackupsBackupsCreateKindErrorComponent
    from ..models.api_v1_backups_backups_create_labels_error_component import (
        ApiV1BackupsBackupsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_metadata_error_component import (
        ApiV1BackupsBackupsCreateMetadataErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_name_error_component import ApiV1BackupsBackupsCreateNameErrorComponent
    from ..models.api_v1_backups_backups_create_non_field_errors_error_component import (
        ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_platform_service_error_component import (
        ApiV1BackupsBackupsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_provider_error_component import (
        ApiV1BackupsBackupsCreateProviderErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_provider_id_error_component import (
        ApiV1BackupsBackupsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_provider_reference_error_component import (
        ApiV1BackupsBackupsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_reconciliation_enabled_error_component import (
        ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_retention_policy_error_component import (
        ApiV1BackupsBackupsCreateRetentionPolicyErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_schedule_error_component import (
        ApiV1BackupsBackupsCreateScheduleErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_size_bytes_error_component import (
        ApiV1BackupsBackupsCreateSizeBytesErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_sla_availability_error_component import (
        ApiV1BackupsBackupsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_sla_target_error_component import (
        ApiV1BackupsBackupsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_slo_availability_error_component import (
        ApiV1BackupsBackupsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_slo_target_error_component import (
        ApiV1BackupsBackupsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_source_namespace_error_component import (
        ApiV1BackupsBackupsCreateSourceNamespaceErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_started_at_error_component import (
        ApiV1BackupsBackupsCreateStartedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_status_error_component import (
        ApiV1BackupsBackupsCreateStatusErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_target_availability_error_component import (
        ApiV1BackupsBackupsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backups_create_tolerations_error_component import (
        ApiV1BackupsBackupsCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BackupsBackupsCreateValidationError")


@_attrs_define
class ApiV1BackupsBackupsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BackupsBackupsCreateAnnotationsErrorComponent |
            ApiV1BackupsBackupsCreateArchivedAtErrorComponent | ApiV1BackupsBackupsCreateArchivedErrorComponent |
            ApiV1BackupsBackupsCreateArchivedReasonErrorComponent | ApiV1BackupsBackupsCreateCompletedAtErrorComponent |
            ApiV1BackupsBackupsCreateCriticalityErrorComponent | ApiV1BackupsBackupsCreateDebugModeErrorComponent |
            ApiV1BackupsBackupsCreateDisplayNameErrorComponent | ApiV1BackupsBackupsCreateExpirationErrorComponent |
            ApiV1BackupsBackupsCreateItemsBackedUpErrorComponent | ApiV1BackupsBackupsCreateK8SClusterErrorComponent |
            ApiV1BackupsBackupsCreateKindErrorComponent | ApiV1BackupsBackupsCreateLabelsErrorComponent |
            ApiV1BackupsBackupsCreateMetadataErrorComponent | ApiV1BackupsBackupsCreateNameErrorComponent |
            ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponent | ApiV1BackupsBackupsCreatePlatformServiceErrorComponent |
            ApiV1BackupsBackupsCreateProviderErrorComponent | ApiV1BackupsBackupsCreateProviderIdErrorComponent |
            ApiV1BackupsBackupsCreateProviderReferenceErrorComponent |
            ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponent |
            ApiV1BackupsBackupsCreateRetentionPolicyErrorComponent | ApiV1BackupsBackupsCreateScheduleErrorComponent |
            ApiV1BackupsBackupsCreateSizeBytesErrorComponent | ApiV1BackupsBackupsCreateSlaAvailabilityErrorComponent |
            ApiV1BackupsBackupsCreateSlaTargetErrorComponent | ApiV1BackupsBackupsCreateSloAvailabilityErrorComponent |
            ApiV1BackupsBackupsCreateSloTargetErrorComponent | ApiV1BackupsBackupsCreateSourceNamespaceErrorComponent |
            ApiV1BackupsBackupsCreateStartedAtErrorComponent | ApiV1BackupsBackupsCreateStatusErrorComponent |
            ApiV1BackupsBackupsCreateTargetAvailabilityErrorComponent |
            ApiV1BackupsBackupsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BackupsBackupsCreateAnnotationsErrorComponent
        | ApiV1BackupsBackupsCreateArchivedAtErrorComponent
        | ApiV1BackupsBackupsCreateArchivedErrorComponent
        | ApiV1BackupsBackupsCreateArchivedReasonErrorComponent
        | ApiV1BackupsBackupsCreateCompletedAtErrorComponent
        | ApiV1BackupsBackupsCreateCriticalityErrorComponent
        | ApiV1BackupsBackupsCreateDebugModeErrorComponent
        | ApiV1BackupsBackupsCreateDisplayNameErrorComponent
        | ApiV1BackupsBackupsCreateExpirationErrorComponent
        | ApiV1BackupsBackupsCreateItemsBackedUpErrorComponent
        | ApiV1BackupsBackupsCreateK8SClusterErrorComponent
        | ApiV1BackupsBackupsCreateKindErrorComponent
        | ApiV1BackupsBackupsCreateLabelsErrorComponent
        | ApiV1BackupsBackupsCreateMetadataErrorComponent
        | ApiV1BackupsBackupsCreateNameErrorComponent
        | ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponent
        | ApiV1BackupsBackupsCreatePlatformServiceErrorComponent
        | ApiV1BackupsBackupsCreateProviderErrorComponent
        | ApiV1BackupsBackupsCreateProviderIdErrorComponent
        | ApiV1BackupsBackupsCreateProviderReferenceErrorComponent
        | ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponent
        | ApiV1BackupsBackupsCreateRetentionPolicyErrorComponent
        | ApiV1BackupsBackupsCreateScheduleErrorComponent
        | ApiV1BackupsBackupsCreateSizeBytesErrorComponent
        | ApiV1BackupsBackupsCreateSlaAvailabilityErrorComponent
        | ApiV1BackupsBackupsCreateSlaTargetErrorComponent
        | ApiV1BackupsBackupsCreateSloAvailabilityErrorComponent
        | ApiV1BackupsBackupsCreateSloTargetErrorComponent
        | ApiV1BackupsBackupsCreateSourceNamespaceErrorComponent
        | ApiV1BackupsBackupsCreateStartedAtErrorComponent
        | ApiV1BackupsBackupsCreateStatusErrorComponent
        | ApiV1BackupsBackupsCreateTargetAvailabilityErrorComponent
        | ApiV1BackupsBackupsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_backups_backups_create_annotations_error_component import (
            ApiV1BackupsBackupsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_archived_at_error_component import (
            ApiV1BackupsBackupsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_archived_error_component import (
            ApiV1BackupsBackupsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_archived_reason_error_component import (
            ApiV1BackupsBackupsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_completed_at_error_component import (
            ApiV1BackupsBackupsCreateCompletedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_criticality_error_component import (
            ApiV1BackupsBackupsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_debug_mode_error_component import (
            ApiV1BackupsBackupsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_display_name_error_component import (
            ApiV1BackupsBackupsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_expiration_error_component import (
            ApiV1BackupsBackupsCreateExpirationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_items_backed_up_error_component import (
            ApiV1BackupsBackupsCreateItemsBackedUpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_k8s_cluster_error_component import (
            ApiV1BackupsBackupsCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_kind_error_component import (
            ApiV1BackupsBackupsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_labels_error_component import (
            ApiV1BackupsBackupsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_name_error_component import (
            ApiV1BackupsBackupsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_non_field_errors_error_component import (
            ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_platform_service_error_component import (
            ApiV1BackupsBackupsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_provider_error_component import (
            ApiV1BackupsBackupsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_provider_id_error_component import (
            ApiV1BackupsBackupsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_provider_reference_error_component import (
            ApiV1BackupsBackupsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_retention_policy_error_component import (
            ApiV1BackupsBackupsCreateRetentionPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_schedule_error_component import (
            ApiV1BackupsBackupsCreateScheduleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_size_bytes_error_component import (
            ApiV1BackupsBackupsCreateSizeBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_sla_availability_error_component import (
            ApiV1BackupsBackupsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_sla_target_error_component import (
            ApiV1BackupsBackupsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_slo_availability_error_component import (
            ApiV1BackupsBackupsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_slo_target_error_component import (
            ApiV1BackupsBackupsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_source_namespace_error_component import (
            ApiV1BackupsBackupsCreateSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_started_at_error_component import (
            ApiV1BackupsBackupsCreateStartedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_status_error_component import (
            ApiV1BackupsBackupsCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_target_availability_error_component import (
            ApiV1BackupsBackupsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_tolerations_error_component import (
            ApiV1BackupsBackupsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateSourceNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateScheduleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateStartedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateCompletedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateExpirationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateSizeBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateItemsBackedUpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsCreateRetentionPolicyErrorComponent):
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
        from ..models.api_v1_backups_backups_create_annotations_error_component import (
            ApiV1BackupsBackupsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_archived_at_error_component import (
            ApiV1BackupsBackupsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_archived_error_component import (
            ApiV1BackupsBackupsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_archived_reason_error_component import (
            ApiV1BackupsBackupsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_completed_at_error_component import (
            ApiV1BackupsBackupsCreateCompletedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_criticality_error_component import (
            ApiV1BackupsBackupsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_debug_mode_error_component import (
            ApiV1BackupsBackupsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_display_name_error_component import (
            ApiV1BackupsBackupsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_expiration_error_component import (
            ApiV1BackupsBackupsCreateExpirationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_items_backed_up_error_component import (
            ApiV1BackupsBackupsCreateItemsBackedUpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_k8s_cluster_error_component import (
            ApiV1BackupsBackupsCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_kind_error_component import (
            ApiV1BackupsBackupsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_labels_error_component import (
            ApiV1BackupsBackupsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_metadata_error_component import (
            ApiV1BackupsBackupsCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_name_error_component import (
            ApiV1BackupsBackupsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_non_field_errors_error_component import (
            ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_platform_service_error_component import (
            ApiV1BackupsBackupsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_provider_error_component import (
            ApiV1BackupsBackupsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_provider_id_error_component import (
            ApiV1BackupsBackupsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_provider_reference_error_component import (
            ApiV1BackupsBackupsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_retention_policy_error_component import (
            ApiV1BackupsBackupsCreateRetentionPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_schedule_error_component import (
            ApiV1BackupsBackupsCreateScheduleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_size_bytes_error_component import (
            ApiV1BackupsBackupsCreateSizeBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_sla_availability_error_component import (
            ApiV1BackupsBackupsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_sla_target_error_component import (
            ApiV1BackupsBackupsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_slo_availability_error_component import (
            ApiV1BackupsBackupsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_slo_target_error_component import (
            ApiV1BackupsBackupsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_source_namespace_error_component import (
            ApiV1BackupsBackupsCreateSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_started_at_error_component import (
            ApiV1BackupsBackupsCreateStartedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_status_error_component import (
            ApiV1BackupsBackupsCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_target_availability_error_component import (
            ApiV1BackupsBackupsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_create_tolerations_error_component import (
            ApiV1BackupsBackupsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BackupsBackupsCreateAnnotationsErrorComponent
                | ApiV1BackupsBackupsCreateArchivedAtErrorComponent
                | ApiV1BackupsBackupsCreateArchivedErrorComponent
                | ApiV1BackupsBackupsCreateArchivedReasonErrorComponent
                | ApiV1BackupsBackupsCreateCompletedAtErrorComponent
                | ApiV1BackupsBackupsCreateCriticalityErrorComponent
                | ApiV1BackupsBackupsCreateDebugModeErrorComponent
                | ApiV1BackupsBackupsCreateDisplayNameErrorComponent
                | ApiV1BackupsBackupsCreateExpirationErrorComponent
                | ApiV1BackupsBackupsCreateItemsBackedUpErrorComponent
                | ApiV1BackupsBackupsCreateK8SClusterErrorComponent
                | ApiV1BackupsBackupsCreateKindErrorComponent
                | ApiV1BackupsBackupsCreateLabelsErrorComponent
                | ApiV1BackupsBackupsCreateMetadataErrorComponent
                | ApiV1BackupsBackupsCreateNameErrorComponent
                | ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponent
                | ApiV1BackupsBackupsCreatePlatformServiceErrorComponent
                | ApiV1BackupsBackupsCreateProviderErrorComponent
                | ApiV1BackupsBackupsCreateProviderIdErrorComponent
                | ApiV1BackupsBackupsCreateProviderReferenceErrorComponent
                | ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponent
                | ApiV1BackupsBackupsCreateRetentionPolicyErrorComponent
                | ApiV1BackupsBackupsCreateScheduleErrorComponent
                | ApiV1BackupsBackupsCreateSizeBytesErrorComponent
                | ApiV1BackupsBackupsCreateSlaAvailabilityErrorComponent
                | ApiV1BackupsBackupsCreateSlaTargetErrorComponent
                | ApiV1BackupsBackupsCreateSloAvailabilityErrorComponent
                | ApiV1BackupsBackupsCreateSloTargetErrorComponent
                | ApiV1BackupsBackupsCreateSourceNamespaceErrorComponent
                | ApiV1BackupsBackupsCreateStartedAtErrorComponent
                | ApiV1BackupsBackupsCreateStatusErrorComponent
                | ApiV1BackupsBackupsCreateTargetAvailabilityErrorComponent
                | ApiV1BackupsBackupsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_0 = (
                        ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_1 = (
                        ApiV1BackupsBackupsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_2 = (
                        ApiV1BackupsBackupsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_3 = (
                        ApiV1BackupsBackupsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_4 = (
                        ApiV1BackupsBackupsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_5 = (
                        ApiV1BackupsBackupsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_6 = (
                        ApiV1BackupsBackupsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_7 = (
                        ApiV1BackupsBackupsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_8 = (
                        ApiV1BackupsBackupsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_9 = (
                        ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_10 = (
                        ApiV1BackupsBackupsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_11 = (
                        ApiV1BackupsBackupsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_12 = (
                        ApiV1BackupsBackupsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_13 = (
                        ApiV1BackupsBackupsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_14 = (
                        ApiV1BackupsBackupsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_15 = (
                        ApiV1BackupsBackupsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_16 = (
                        ApiV1BackupsBackupsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_17 = (
                        ApiV1BackupsBackupsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_18 = (
                        ApiV1BackupsBackupsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_19 = (
                        ApiV1BackupsBackupsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_20 = (
                        ApiV1BackupsBackupsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_21 = (
                        ApiV1BackupsBackupsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_22 = (
                        ApiV1BackupsBackupsCreateSourceNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_23 = (
                        ApiV1BackupsBackupsCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_24 = (
                        ApiV1BackupsBackupsCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_25 = (
                        ApiV1BackupsBackupsCreateScheduleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_26 = (
                        ApiV1BackupsBackupsCreateStartedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_27 = (
                        ApiV1BackupsBackupsCreateCompletedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_28 = (
                        ApiV1BackupsBackupsCreateExpirationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_29 = (
                        ApiV1BackupsBackupsCreateSizeBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_30 = (
                        ApiV1BackupsBackupsCreateItemsBackedUpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_create_error_type_31 = (
                        ApiV1BackupsBackupsCreateRetentionPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backups_create_error_type_32 = (
                    ApiV1BackupsBackupsCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backups_create_error_type_32

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_backups_backups_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_backups_backups_create_validation_error.additional_properties = d
        return api_v1_backups_backups_create_validation_error

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
