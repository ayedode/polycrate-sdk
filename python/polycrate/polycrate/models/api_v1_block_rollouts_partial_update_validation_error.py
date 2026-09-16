from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollouts_partial_update_actual_availability_error_component import (
        ApiV1BlockRolloutsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_annotations_error_component import (
        ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_archived_at_error_component import (
        ApiV1BlockRolloutsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_archived_error_component import (
        ApiV1BlockRolloutsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_archived_reason_error_component import (
        ApiV1BlockRolloutsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_batch_identifier_error_component import (
        ApiV1BlockRolloutsPartialUpdateBatchIdentifierErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_completed_items_error_component import (
        ApiV1BlockRolloutsPartialUpdateCompletedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_conditions_error_component import (
        ApiV1BlockRolloutsPartialUpdateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_criticality_error_component import (
        ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_debug_mode_error_component import (
        ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_discovery_enabled_error_component import (
        ApiV1BlockRolloutsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_discovery_running_error_component import (
        ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_discovery_task_id_error_component import (
        ApiV1BlockRolloutsPartialUpdateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_discovery_task_meta_error_component import (
        ApiV1BlockRolloutsPartialUpdateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_dispatched_items_error_component import (
        ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_display_name_error_component import (
        ApiV1BlockRolloutsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_failed_items_error_component import (
        ApiV1BlockRolloutsPartialUpdateFailedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_kind_error_component import (
        ApiV1BlockRolloutsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_labels_error_component import (
        ApiV1BlockRolloutsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_last_item_added_at_error_component import (
        ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_last_state_change_error_component import (
        ApiV1BlockRolloutsPartialUpdateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_last_state_error_component import (
        ApiV1BlockRolloutsPartialUpdateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_name_error_component import (
        ApiV1BlockRolloutsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_non_field_errors_error_component import (
        ApiV1BlockRolloutsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_platform_service_error_component import (
        ApiV1BlockRolloutsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_provider_error_component import (
        ApiV1BlockRolloutsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_provider_id_error_component import (
        ApiV1BlockRolloutsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_provider_reference_error_component import (
        ApiV1BlockRolloutsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_quiescence_seconds_error_component import (
        ApiV1BlockRolloutsPartialUpdateQuiescenceSecondsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_reconciliation_running_error_component import (
        ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutsPartialUpdateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutsPartialUpdateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_repair_running_error_component import (
        ApiV1BlockRolloutsPartialUpdateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_repair_task_id_error_component import (
        ApiV1BlockRolloutsPartialUpdateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_repair_task_meta_error_component import (
        ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_scope_error_component import (
        ApiV1BlockRolloutsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_sla_availability_error_component import (
        ApiV1BlockRolloutsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_sla_target_error_component import (
        ApiV1BlockRolloutsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_slo_availability_error_component import (
        ApiV1BlockRolloutsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_slo_target_error_component import (
        ApiV1BlockRolloutsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_state_error_component import (
        ApiV1BlockRolloutsPartialUpdateStateErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_state_reason_error_component import (
        ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_status_error_component import (
        ApiV1BlockRolloutsPartialUpdateStatusErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_target_availability_error_component import (
        ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_tolerations_error_component import (
        ApiV1BlockRolloutsPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_partial_update_total_items_error_component import (
        ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutsPartialUpdateValidationError")


@_attrs_define
class ApiV1BlockRolloutsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponent |
            ApiV1BlockRolloutsPartialUpdateArchivedAtErrorComponent | ApiV1BlockRolloutsPartialUpdateArchivedErrorComponent
            | ApiV1BlockRolloutsPartialUpdateArchivedReasonErrorComponent |
            ApiV1BlockRolloutsPartialUpdateBatchIdentifierErrorComponent |
            ApiV1BlockRolloutsPartialUpdateCompletedItemsErrorComponent |
            ApiV1BlockRolloutsPartialUpdateConditionsErrorComponent |
            ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponent |
            ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponent |
            ApiV1BlockRolloutsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutsPartialUpdateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutsPartialUpdateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponent |
            ApiV1BlockRolloutsPartialUpdateDisplayNameErrorComponent |
            ApiV1BlockRolloutsPartialUpdateFailedItemsErrorComponent | ApiV1BlockRolloutsPartialUpdateKindErrorComponent |
            ApiV1BlockRolloutsPartialUpdateLabelsErrorComponent |
            ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponent |
            ApiV1BlockRolloutsPartialUpdateLastStateChangeErrorComponent |
            ApiV1BlockRolloutsPartialUpdateLastStateErrorComponent | ApiV1BlockRolloutsPartialUpdateNameErrorComponent |
            ApiV1BlockRolloutsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutsPartialUpdatePlatformServiceErrorComponent |
            ApiV1BlockRolloutsPartialUpdateProviderErrorComponent | ApiV1BlockRolloutsPartialUpdateProviderIdErrorComponent
            | ApiV1BlockRolloutsPartialUpdateProviderReferenceErrorComponent |
            ApiV1BlockRolloutsPartialUpdateQuiescenceSecondsErrorComponent |
            ApiV1BlockRolloutsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutsPartialUpdateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutsPartialUpdateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutsPartialUpdateRepairRunningErrorComponent |
            ApiV1BlockRolloutsPartialUpdateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponent | ApiV1BlockRolloutsPartialUpdateScopeErrorComponent
            | ApiV1BlockRolloutsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutsPartialUpdateSlaTargetErrorComponent |
            ApiV1BlockRolloutsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1BlockRolloutsPartialUpdateSloTargetErrorComponent | ApiV1BlockRolloutsPartialUpdateStateErrorComponent |
            ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponent | ApiV1BlockRolloutsPartialUpdateStatusErrorComponent |
            ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutsPartialUpdateTolerationsErrorComponent |
            ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponent
        | ApiV1BlockRolloutsPartialUpdateArchivedAtErrorComponent
        | ApiV1BlockRolloutsPartialUpdateArchivedErrorComponent
        | ApiV1BlockRolloutsPartialUpdateArchivedReasonErrorComponent
        | ApiV1BlockRolloutsPartialUpdateBatchIdentifierErrorComponent
        | ApiV1BlockRolloutsPartialUpdateCompletedItemsErrorComponent
        | ApiV1BlockRolloutsPartialUpdateConditionsErrorComponent
        | ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponent
        | ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponent
        | ApiV1BlockRolloutsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutsPartialUpdateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutsPartialUpdateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponent
        | ApiV1BlockRolloutsPartialUpdateDisplayNameErrorComponent
        | ApiV1BlockRolloutsPartialUpdateFailedItemsErrorComponent
        | ApiV1BlockRolloutsPartialUpdateKindErrorComponent
        | ApiV1BlockRolloutsPartialUpdateLabelsErrorComponent
        | ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponent
        | ApiV1BlockRolloutsPartialUpdateLastStateChangeErrorComponent
        | ApiV1BlockRolloutsPartialUpdateLastStateErrorComponent
        | ApiV1BlockRolloutsPartialUpdateNameErrorComponent
        | ApiV1BlockRolloutsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutsPartialUpdatePlatformServiceErrorComponent
        | ApiV1BlockRolloutsPartialUpdateProviderErrorComponent
        | ApiV1BlockRolloutsPartialUpdateProviderIdErrorComponent
        | ApiV1BlockRolloutsPartialUpdateProviderReferenceErrorComponent
        | ApiV1BlockRolloutsPartialUpdateQuiescenceSecondsErrorComponent
        | ApiV1BlockRolloutsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutsPartialUpdateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutsPartialUpdateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutsPartialUpdateRepairRunningErrorComponent
        | ApiV1BlockRolloutsPartialUpdateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutsPartialUpdateScopeErrorComponent
        | ApiV1BlockRolloutsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutsPartialUpdateSlaTargetErrorComponent
        | ApiV1BlockRolloutsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutsPartialUpdateSloTargetErrorComponent
        | ApiV1BlockRolloutsPartialUpdateStateErrorComponent
        | ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponent
        | ApiV1BlockRolloutsPartialUpdateStatusErrorComponent
        | ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutsPartialUpdateTolerationsErrorComponent
        | ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollouts_partial_update_actual_availability_error_component import (
            ApiV1BlockRolloutsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_annotations_error_component import (
            ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_archived_at_error_component import (
            ApiV1BlockRolloutsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_archived_error_component import (
            ApiV1BlockRolloutsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_archived_reason_error_component import (
            ApiV1BlockRolloutsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_batch_identifier_error_component import (
            ApiV1BlockRolloutsPartialUpdateBatchIdentifierErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_completed_items_error_component import (
            ApiV1BlockRolloutsPartialUpdateCompletedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_conditions_error_component import (
            ApiV1BlockRolloutsPartialUpdateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_criticality_error_component import (
            ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_debug_mode_error_component import (
            ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_discovery_running_error_component import (
            ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutsPartialUpdateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutsPartialUpdateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_dispatched_items_error_component import (
            ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_display_name_error_component import (
            ApiV1BlockRolloutsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_failed_items_error_component import (
            ApiV1BlockRolloutsPartialUpdateFailedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_kind_error_component import (
            ApiV1BlockRolloutsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_labels_error_component import (
            ApiV1BlockRolloutsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_last_item_added_at_error_component import (
            ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_last_state_change_error_component import (
            ApiV1BlockRolloutsPartialUpdateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_last_state_error_component import (
            ApiV1BlockRolloutsPartialUpdateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_name_error_component import (
            ApiV1BlockRolloutsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_non_field_errors_error_component import (
            ApiV1BlockRolloutsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_platform_service_error_component import (
            ApiV1BlockRolloutsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_provider_error_component import (
            ApiV1BlockRolloutsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_provider_id_error_component import (
            ApiV1BlockRolloutsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_provider_reference_error_component import (
            ApiV1BlockRolloutsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutsPartialUpdateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutsPartialUpdateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_repair_running_error_component import (
            ApiV1BlockRolloutsPartialUpdateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_repair_task_id_error_component import (
            ApiV1BlockRolloutsPartialUpdateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_scope_error_component import (
            ApiV1BlockRolloutsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_sla_availability_error_component import (
            ApiV1BlockRolloutsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_sla_target_error_component import (
            ApiV1BlockRolloutsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_slo_availability_error_component import (
            ApiV1BlockRolloutsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_slo_target_error_component import (
            ApiV1BlockRolloutsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_state_error_component import (
            ApiV1BlockRolloutsPartialUpdateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_state_reason_error_component import (
            ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_status_error_component import (
            ApiV1BlockRolloutsPartialUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_target_availability_error_component import (
            ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_tolerations_error_component import (
            ApiV1BlockRolloutsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_total_items_error_component import (
            ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateBatchIdentifierErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateCompletedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateFailedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponent):
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
        from ..models.api_v1_block_rollouts_partial_update_actual_availability_error_component import (
            ApiV1BlockRolloutsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_annotations_error_component import (
            ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_archived_at_error_component import (
            ApiV1BlockRolloutsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_archived_error_component import (
            ApiV1BlockRolloutsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_archived_reason_error_component import (
            ApiV1BlockRolloutsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_batch_identifier_error_component import (
            ApiV1BlockRolloutsPartialUpdateBatchIdentifierErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_completed_items_error_component import (
            ApiV1BlockRolloutsPartialUpdateCompletedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_conditions_error_component import (
            ApiV1BlockRolloutsPartialUpdateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_criticality_error_component import (
            ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_debug_mode_error_component import (
            ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_discovery_running_error_component import (
            ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutsPartialUpdateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutsPartialUpdateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_dispatched_items_error_component import (
            ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_display_name_error_component import (
            ApiV1BlockRolloutsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_failed_items_error_component import (
            ApiV1BlockRolloutsPartialUpdateFailedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_kind_error_component import (
            ApiV1BlockRolloutsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_labels_error_component import (
            ApiV1BlockRolloutsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_last_item_added_at_error_component import (
            ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_last_state_change_error_component import (
            ApiV1BlockRolloutsPartialUpdateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_last_state_error_component import (
            ApiV1BlockRolloutsPartialUpdateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_name_error_component import (
            ApiV1BlockRolloutsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_non_field_errors_error_component import (
            ApiV1BlockRolloutsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_platform_service_error_component import (
            ApiV1BlockRolloutsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_provider_error_component import (
            ApiV1BlockRolloutsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_provider_id_error_component import (
            ApiV1BlockRolloutsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_provider_reference_error_component import (
            ApiV1BlockRolloutsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_quiescence_seconds_error_component import (
            ApiV1BlockRolloutsPartialUpdateQuiescenceSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutsPartialUpdateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutsPartialUpdateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_repair_running_error_component import (
            ApiV1BlockRolloutsPartialUpdateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_repair_task_id_error_component import (
            ApiV1BlockRolloutsPartialUpdateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_scope_error_component import (
            ApiV1BlockRolloutsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_sla_availability_error_component import (
            ApiV1BlockRolloutsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_sla_target_error_component import (
            ApiV1BlockRolloutsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_slo_availability_error_component import (
            ApiV1BlockRolloutsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_slo_target_error_component import (
            ApiV1BlockRolloutsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_state_error_component import (
            ApiV1BlockRolloutsPartialUpdateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_state_reason_error_component import (
            ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_status_error_component import (
            ApiV1BlockRolloutsPartialUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_target_availability_error_component import (
            ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_tolerations_error_component import (
            ApiV1BlockRolloutsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_partial_update_total_items_error_component import (
            ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponent
                | ApiV1BlockRolloutsPartialUpdateArchivedAtErrorComponent
                | ApiV1BlockRolloutsPartialUpdateArchivedErrorComponent
                | ApiV1BlockRolloutsPartialUpdateArchivedReasonErrorComponent
                | ApiV1BlockRolloutsPartialUpdateBatchIdentifierErrorComponent
                | ApiV1BlockRolloutsPartialUpdateCompletedItemsErrorComponent
                | ApiV1BlockRolloutsPartialUpdateConditionsErrorComponent
                | ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponent
                | ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponent
                | ApiV1BlockRolloutsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutsPartialUpdateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutsPartialUpdateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponent
                | ApiV1BlockRolloutsPartialUpdateDisplayNameErrorComponent
                | ApiV1BlockRolloutsPartialUpdateFailedItemsErrorComponent
                | ApiV1BlockRolloutsPartialUpdateKindErrorComponent
                | ApiV1BlockRolloutsPartialUpdateLabelsErrorComponent
                | ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponent
                | ApiV1BlockRolloutsPartialUpdateLastStateChangeErrorComponent
                | ApiV1BlockRolloutsPartialUpdateLastStateErrorComponent
                | ApiV1BlockRolloutsPartialUpdateNameErrorComponent
                | ApiV1BlockRolloutsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutsPartialUpdatePlatformServiceErrorComponent
                | ApiV1BlockRolloutsPartialUpdateProviderErrorComponent
                | ApiV1BlockRolloutsPartialUpdateProviderIdErrorComponent
                | ApiV1BlockRolloutsPartialUpdateProviderReferenceErrorComponent
                | ApiV1BlockRolloutsPartialUpdateQuiescenceSecondsErrorComponent
                | ApiV1BlockRolloutsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutsPartialUpdateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutsPartialUpdateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutsPartialUpdateRepairRunningErrorComponent
                | ApiV1BlockRolloutsPartialUpdateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutsPartialUpdateScopeErrorComponent
                | ApiV1BlockRolloutsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutsPartialUpdateSlaTargetErrorComponent
                | ApiV1BlockRolloutsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutsPartialUpdateSloTargetErrorComponent
                | ApiV1BlockRolloutsPartialUpdateStateErrorComponent
                | ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponent
                | ApiV1BlockRolloutsPartialUpdateStatusErrorComponent
                | ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutsPartialUpdateTolerationsErrorComponent
                | ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_0 = (
                        ApiV1BlockRolloutsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_1 = (
                        ApiV1BlockRolloutsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_2 = (
                        ApiV1BlockRolloutsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_3 = (
                        ApiV1BlockRolloutsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_4 = (
                        ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_5 = (
                        ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_6 = (
                        ApiV1BlockRolloutsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_7 = (
                        ApiV1BlockRolloutsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_8 = (
                        ApiV1BlockRolloutsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_9 = (
                        ApiV1BlockRolloutsPartialUpdateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_10 = (
                        ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_11 = (
                        ApiV1BlockRolloutsPartialUpdateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_12 = (
                        ApiV1BlockRolloutsPartialUpdateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_13 = (
                        ApiV1BlockRolloutsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_14 = (
                        ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_15 = (
                        ApiV1BlockRolloutsPartialUpdateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_16 = (
                        ApiV1BlockRolloutsPartialUpdateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_17 = (
                        ApiV1BlockRolloutsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_18 = (
                        ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_19 = (
                        ApiV1BlockRolloutsPartialUpdateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_20 = (
                        ApiV1BlockRolloutsPartialUpdateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_21 = (
                        ApiV1BlockRolloutsPartialUpdateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_22 = (
                        ApiV1BlockRolloutsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_23 = (
                        ApiV1BlockRolloutsPartialUpdateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_24 = (
                        ApiV1BlockRolloutsPartialUpdateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_25 = (
                        ApiV1BlockRolloutsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_26 = (
                        ApiV1BlockRolloutsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_27 = (
                        ApiV1BlockRolloutsPartialUpdateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_28 = (
                        ApiV1BlockRolloutsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_29 = (
                        ApiV1BlockRolloutsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_30 = (
                        ApiV1BlockRolloutsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_31 = (
                        ApiV1BlockRolloutsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_32 = (
                        ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_33 = (
                        ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_34 = (
                        ApiV1BlockRolloutsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_35 = (
                        ApiV1BlockRolloutsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_36 = (
                        ApiV1BlockRolloutsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_37 = (
                        ApiV1BlockRolloutsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_38 = (
                        ApiV1BlockRolloutsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_39 = (
                        ApiV1BlockRolloutsPartialUpdateBatchIdentifierErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_40 = (
                        ApiV1BlockRolloutsPartialUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_41 = (
                        ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_42 = (
                        ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_43 = (
                        ApiV1BlockRolloutsPartialUpdateCompletedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_44 = (
                        ApiV1BlockRolloutsPartialUpdateFailedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_partial_update_error_type_45 = (
                        ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollouts_partial_update_error_type_46 = (
                    ApiV1BlockRolloutsPartialUpdateQuiescenceSecondsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollouts_partial_update_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollouts_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollouts_partial_update_validation_error.additional_properties = d
        return api_v1_block_rollouts_partial_update_validation_error

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
