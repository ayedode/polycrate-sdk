from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollouts_archive_create_actual_availability_error_component import (
        ApiV1BlockRolloutsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_annotations_error_component import (
        ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_archived_at_error_component import (
        ApiV1BlockRolloutsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_archived_error_component import (
        ApiV1BlockRolloutsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_archived_reason_error_component import (
        ApiV1BlockRolloutsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_batch_identifier_error_component import (
        ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_completed_items_error_component import (
        ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_conditions_error_component import (
        ApiV1BlockRolloutsArchiveCreateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_criticality_error_component import (
        ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_debug_mode_error_component import (
        ApiV1BlockRolloutsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_discovery_enabled_error_component import (
        ApiV1BlockRolloutsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_discovery_running_error_component import (
        ApiV1BlockRolloutsArchiveCreateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_discovery_task_id_error_component import (
        ApiV1BlockRolloutsArchiveCreateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_discovery_task_meta_error_component import (
        ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_dispatched_items_error_component import (
        ApiV1BlockRolloutsArchiveCreateDispatchedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_display_name_error_component import (
        ApiV1BlockRolloutsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_failed_items_error_component import (
        ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_kind_error_component import (
        ApiV1BlockRolloutsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_labels_error_component import (
        ApiV1BlockRolloutsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_last_item_added_at_error_component import (
        ApiV1BlockRolloutsArchiveCreateLastItemAddedAtErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_last_state_change_error_component import (
        ApiV1BlockRolloutsArchiveCreateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_last_state_error_component import (
        ApiV1BlockRolloutsArchiveCreateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_name_error_component import (
        ApiV1BlockRolloutsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_non_field_errors_error_component import (
        ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_platform_service_error_component import (
        ApiV1BlockRolloutsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_provider_error_component import (
        ApiV1BlockRolloutsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_provider_id_error_component import (
        ApiV1BlockRolloutsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_provider_reference_error_component import (
        ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_quiescence_seconds_error_component import (
        ApiV1BlockRolloutsArchiveCreateQuiescenceSecondsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_reconciliation_running_error_component import (
        ApiV1BlockRolloutsArchiveCreateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutsArchiveCreateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutsArchiveCreateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_repair_running_error_component import (
        ApiV1BlockRolloutsArchiveCreateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_repair_task_id_error_component import (
        ApiV1BlockRolloutsArchiveCreateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_repair_task_meta_error_component import (
        ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_scope_error_component import (
        ApiV1BlockRolloutsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_sla_availability_error_component import (
        ApiV1BlockRolloutsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_sla_target_error_component import (
        ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_slo_availability_error_component import (
        ApiV1BlockRolloutsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_slo_target_error_component import (
        ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_state_error_component import (
        ApiV1BlockRolloutsArchiveCreateStateErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_state_reason_error_component import (
        ApiV1BlockRolloutsArchiveCreateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_status_error_component import (
        ApiV1BlockRolloutsArchiveCreateStatusErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_target_availability_error_component import (
        ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_tolerations_error_component import (
        ApiV1BlockRolloutsArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_archive_create_total_items_error_component import (
        ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutsArchiveCreateValidationError")


@_attrs_define
class ApiV1BlockRolloutsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponent |
            ApiV1BlockRolloutsArchiveCreateArchivedAtErrorComponent | ApiV1BlockRolloutsArchiveCreateArchivedErrorComponent
            | ApiV1BlockRolloutsArchiveCreateArchivedReasonErrorComponent |
            ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponent |
            ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponent |
            ApiV1BlockRolloutsArchiveCreateConditionsErrorComponent |
            ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponent |
            ApiV1BlockRolloutsArchiveCreateDebugModeErrorComponent |
            ApiV1BlockRolloutsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutsArchiveCreateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutsArchiveCreateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutsArchiveCreateDispatchedItemsErrorComponent |
            ApiV1BlockRolloutsArchiveCreateDisplayNameErrorComponent |
            ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponent | ApiV1BlockRolloutsArchiveCreateKindErrorComponent |
            ApiV1BlockRolloutsArchiveCreateLabelsErrorComponent |
            ApiV1BlockRolloutsArchiveCreateLastItemAddedAtErrorComponent |
            ApiV1BlockRolloutsArchiveCreateLastStateChangeErrorComponent |
            ApiV1BlockRolloutsArchiveCreateLastStateErrorComponent | ApiV1BlockRolloutsArchiveCreateNameErrorComponent |
            ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutsArchiveCreatePlatformServiceErrorComponent |
            ApiV1BlockRolloutsArchiveCreateProviderErrorComponent | ApiV1BlockRolloutsArchiveCreateProviderIdErrorComponent
            | ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponent |
            ApiV1BlockRolloutsArchiveCreateQuiescenceSecondsErrorComponent |
            ApiV1BlockRolloutsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutsArchiveCreateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutsArchiveCreateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutsArchiveCreateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutsArchiveCreateRepairRunningErrorComponent |
            ApiV1BlockRolloutsArchiveCreateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponent | ApiV1BlockRolloutsArchiveCreateScopeErrorComponent
            | ApiV1BlockRolloutsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponent |
            ApiV1BlockRolloutsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponent | ApiV1BlockRolloutsArchiveCreateStateErrorComponent |
            ApiV1BlockRolloutsArchiveCreateStateReasonErrorComponent | ApiV1BlockRolloutsArchiveCreateStatusErrorComponent |
            ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutsArchiveCreateTolerationsErrorComponent |
            ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponent
        | ApiV1BlockRolloutsArchiveCreateArchivedAtErrorComponent
        | ApiV1BlockRolloutsArchiveCreateArchivedErrorComponent
        | ApiV1BlockRolloutsArchiveCreateArchivedReasonErrorComponent
        | ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponent
        | ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponent
        | ApiV1BlockRolloutsArchiveCreateConditionsErrorComponent
        | ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponent
        | ApiV1BlockRolloutsArchiveCreateDebugModeErrorComponent
        | ApiV1BlockRolloutsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutsArchiveCreateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutsArchiveCreateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutsArchiveCreateDispatchedItemsErrorComponent
        | ApiV1BlockRolloutsArchiveCreateDisplayNameErrorComponent
        | ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponent
        | ApiV1BlockRolloutsArchiveCreateKindErrorComponent
        | ApiV1BlockRolloutsArchiveCreateLabelsErrorComponent
        | ApiV1BlockRolloutsArchiveCreateLastItemAddedAtErrorComponent
        | ApiV1BlockRolloutsArchiveCreateLastStateChangeErrorComponent
        | ApiV1BlockRolloutsArchiveCreateLastStateErrorComponent
        | ApiV1BlockRolloutsArchiveCreateNameErrorComponent
        | ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutsArchiveCreatePlatformServiceErrorComponent
        | ApiV1BlockRolloutsArchiveCreateProviderErrorComponent
        | ApiV1BlockRolloutsArchiveCreateProviderIdErrorComponent
        | ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponent
        | ApiV1BlockRolloutsArchiveCreateQuiescenceSecondsErrorComponent
        | ApiV1BlockRolloutsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutsArchiveCreateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutsArchiveCreateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutsArchiveCreateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutsArchiveCreateRepairRunningErrorComponent
        | ApiV1BlockRolloutsArchiveCreateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutsArchiveCreateScopeErrorComponent
        | ApiV1BlockRolloutsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponent
        | ApiV1BlockRolloutsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponent
        | ApiV1BlockRolloutsArchiveCreateStateErrorComponent
        | ApiV1BlockRolloutsArchiveCreateStateReasonErrorComponent
        | ApiV1BlockRolloutsArchiveCreateStatusErrorComponent
        | ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutsArchiveCreateTolerationsErrorComponent
        | ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollouts_archive_create_actual_availability_error_component import (
            ApiV1BlockRolloutsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_annotations_error_component import (
            ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_archived_at_error_component import (
            ApiV1BlockRolloutsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_archived_error_component import (
            ApiV1BlockRolloutsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_archived_reason_error_component import (
            ApiV1BlockRolloutsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_batch_identifier_error_component import (
            ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_completed_items_error_component import (
            ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_conditions_error_component import (
            ApiV1BlockRolloutsArchiveCreateConditionsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_criticality_error_component import (
            ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_debug_mode_error_component import (
            ApiV1BlockRolloutsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_discovery_running_error_component import (
            ApiV1BlockRolloutsArchiveCreateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutsArchiveCreateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_dispatched_items_error_component import (
            ApiV1BlockRolloutsArchiveCreateDispatchedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_display_name_error_component import (
            ApiV1BlockRolloutsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_failed_items_error_component import (
            ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_kind_error_component import (
            ApiV1BlockRolloutsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_labels_error_component import (
            ApiV1BlockRolloutsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_last_item_added_at_error_component import (
            ApiV1BlockRolloutsArchiveCreateLastItemAddedAtErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_last_state_change_error_component import (
            ApiV1BlockRolloutsArchiveCreateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_last_state_error_component import (
            ApiV1BlockRolloutsArchiveCreateLastStateErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_name_error_component import (
            ApiV1BlockRolloutsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_non_field_errors_error_component import (
            ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_platform_service_error_component import (
            ApiV1BlockRolloutsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_provider_error_component import (
            ApiV1BlockRolloutsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_provider_id_error_component import (
            ApiV1BlockRolloutsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_provider_reference_error_component import (
            ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutsArchiveCreateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutsArchiveCreateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutsArchiveCreateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_repair_running_error_component import (
            ApiV1BlockRolloutsArchiveCreateRepairRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_repair_task_id_error_component import (
            ApiV1BlockRolloutsArchiveCreateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_scope_error_component import (
            ApiV1BlockRolloutsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_sla_availability_error_component import (
            ApiV1BlockRolloutsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_sla_target_error_component import (
            ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_slo_availability_error_component import (
            ApiV1BlockRolloutsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_slo_target_error_component import (
            ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_state_error_component import (
            ApiV1BlockRolloutsArchiveCreateStateErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_state_reason_error_component import (
            ApiV1BlockRolloutsArchiveCreateStateReasonErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_status_error_component import (
            ApiV1BlockRolloutsArchiveCreateStatusErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_target_availability_error_component import (
            ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_tolerations_error_component import (
            ApiV1BlockRolloutsArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_total_items_error_component import (
            ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateDispatchedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsArchiveCreateLastItemAddedAtErrorComponent):
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
        from ..models.api_v1_block_rollouts_archive_create_actual_availability_error_component import (
            ApiV1BlockRolloutsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_annotations_error_component import (
            ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_archived_at_error_component import (
            ApiV1BlockRolloutsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_archived_error_component import (
            ApiV1BlockRolloutsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_archived_reason_error_component import (
            ApiV1BlockRolloutsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_batch_identifier_error_component import (
            ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_completed_items_error_component import (
            ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_conditions_error_component import (
            ApiV1BlockRolloutsArchiveCreateConditionsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_criticality_error_component import (
            ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_debug_mode_error_component import (
            ApiV1BlockRolloutsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_discovery_running_error_component import (
            ApiV1BlockRolloutsArchiveCreateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutsArchiveCreateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_dispatched_items_error_component import (
            ApiV1BlockRolloutsArchiveCreateDispatchedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_display_name_error_component import (
            ApiV1BlockRolloutsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_failed_items_error_component import (
            ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_kind_error_component import (
            ApiV1BlockRolloutsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_labels_error_component import (
            ApiV1BlockRolloutsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_last_item_added_at_error_component import (
            ApiV1BlockRolloutsArchiveCreateLastItemAddedAtErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_last_state_change_error_component import (
            ApiV1BlockRolloutsArchiveCreateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_last_state_error_component import (
            ApiV1BlockRolloutsArchiveCreateLastStateErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_name_error_component import (
            ApiV1BlockRolloutsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_non_field_errors_error_component import (
            ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_platform_service_error_component import (
            ApiV1BlockRolloutsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_provider_error_component import (
            ApiV1BlockRolloutsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_provider_id_error_component import (
            ApiV1BlockRolloutsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_provider_reference_error_component import (
            ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_quiescence_seconds_error_component import (
            ApiV1BlockRolloutsArchiveCreateQuiescenceSecondsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutsArchiveCreateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutsArchiveCreateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutsArchiveCreateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_repair_running_error_component import (
            ApiV1BlockRolloutsArchiveCreateRepairRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_repair_task_id_error_component import (
            ApiV1BlockRolloutsArchiveCreateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_scope_error_component import (
            ApiV1BlockRolloutsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_sla_availability_error_component import (
            ApiV1BlockRolloutsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_sla_target_error_component import (
            ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_slo_availability_error_component import (
            ApiV1BlockRolloutsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_slo_target_error_component import (
            ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_state_error_component import (
            ApiV1BlockRolloutsArchiveCreateStateErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_state_reason_error_component import (
            ApiV1BlockRolloutsArchiveCreateStateReasonErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_status_error_component import (
            ApiV1BlockRolloutsArchiveCreateStatusErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_target_availability_error_component import (
            ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_tolerations_error_component import (
            ApiV1BlockRolloutsArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_archive_create_total_items_error_component import (
            ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponent
                | ApiV1BlockRolloutsArchiveCreateArchivedAtErrorComponent
                | ApiV1BlockRolloutsArchiveCreateArchivedErrorComponent
                | ApiV1BlockRolloutsArchiveCreateArchivedReasonErrorComponent
                | ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponent
                | ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponent
                | ApiV1BlockRolloutsArchiveCreateConditionsErrorComponent
                | ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponent
                | ApiV1BlockRolloutsArchiveCreateDebugModeErrorComponent
                | ApiV1BlockRolloutsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutsArchiveCreateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutsArchiveCreateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutsArchiveCreateDispatchedItemsErrorComponent
                | ApiV1BlockRolloutsArchiveCreateDisplayNameErrorComponent
                | ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponent
                | ApiV1BlockRolloutsArchiveCreateKindErrorComponent
                | ApiV1BlockRolloutsArchiveCreateLabelsErrorComponent
                | ApiV1BlockRolloutsArchiveCreateLastItemAddedAtErrorComponent
                | ApiV1BlockRolloutsArchiveCreateLastStateChangeErrorComponent
                | ApiV1BlockRolloutsArchiveCreateLastStateErrorComponent
                | ApiV1BlockRolloutsArchiveCreateNameErrorComponent
                | ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutsArchiveCreatePlatformServiceErrorComponent
                | ApiV1BlockRolloutsArchiveCreateProviderErrorComponent
                | ApiV1BlockRolloutsArchiveCreateProviderIdErrorComponent
                | ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponent
                | ApiV1BlockRolloutsArchiveCreateQuiescenceSecondsErrorComponent
                | ApiV1BlockRolloutsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutsArchiveCreateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutsArchiveCreateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutsArchiveCreateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutsArchiveCreateRepairRunningErrorComponent
                | ApiV1BlockRolloutsArchiveCreateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutsArchiveCreateScopeErrorComponent
                | ApiV1BlockRolloutsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponent
                | ApiV1BlockRolloutsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponent
                | ApiV1BlockRolloutsArchiveCreateStateErrorComponent
                | ApiV1BlockRolloutsArchiveCreateStateReasonErrorComponent
                | ApiV1BlockRolloutsArchiveCreateStatusErrorComponent
                | ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutsArchiveCreateTolerationsErrorComponent
                | ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_0 = (
                        ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_1 = (
                        ApiV1BlockRolloutsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_2 = (
                        ApiV1BlockRolloutsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_3 = (
                        ApiV1BlockRolloutsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_4 = (
                        ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_5 = (
                        ApiV1BlockRolloutsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_6 = (
                        ApiV1BlockRolloutsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_7 = (
                        ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_8 = (
                        ApiV1BlockRolloutsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_9 = (
                        ApiV1BlockRolloutsArchiveCreateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_10 = (
                        ApiV1BlockRolloutsArchiveCreateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_11 = (
                        ApiV1BlockRolloutsArchiveCreateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_12 = (
                        ApiV1BlockRolloutsArchiveCreateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_13 = (
                        ApiV1BlockRolloutsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_14 = (
                        ApiV1BlockRolloutsArchiveCreateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_15 = (
                        ApiV1BlockRolloutsArchiveCreateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_16 = (
                        ApiV1BlockRolloutsArchiveCreateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_17 = (
                        ApiV1BlockRolloutsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_18 = (
                        ApiV1BlockRolloutsArchiveCreateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_19 = (
                        ApiV1BlockRolloutsArchiveCreateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_20 = (
                        ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_21 = (
                        ApiV1BlockRolloutsArchiveCreateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_22 = (
                        ApiV1BlockRolloutsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_23 = (
                        ApiV1BlockRolloutsArchiveCreateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_24 = (
                        ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_25 = (
                        ApiV1BlockRolloutsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_26 = (
                        ApiV1BlockRolloutsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_27 = (
                        ApiV1BlockRolloutsArchiveCreateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_28 = (
                        ApiV1BlockRolloutsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_29 = (
                        ApiV1BlockRolloutsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_30 = (
                        ApiV1BlockRolloutsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_31 = (
                        ApiV1BlockRolloutsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_32 = (
                        ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_33 = (
                        ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_34 = (
                        ApiV1BlockRolloutsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_35 = (
                        ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_36 = (
                        ApiV1BlockRolloutsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_37 = (
                        ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_38 = (
                        ApiV1BlockRolloutsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_39 = (
                        ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_40 = (
                        ApiV1BlockRolloutsArchiveCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_41 = (
                        ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_42 = (
                        ApiV1BlockRolloutsArchiveCreateDispatchedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_43 = (
                        ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_44 = (
                        ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_archive_create_error_type_45 = (
                        ApiV1BlockRolloutsArchiveCreateLastItemAddedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollouts_archive_create_error_type_46 = (
                    ApiV1BlockRolloutsArchiveCreateQuiescenceSecondsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollouts_archive_create_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollouts_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollouts_archive_create_validation_error.additional_properties = d
        return api_v1_block_rollouts_archive_create_validation_error

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
