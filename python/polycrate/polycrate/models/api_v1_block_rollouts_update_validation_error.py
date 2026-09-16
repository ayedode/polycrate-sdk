from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollouts_update_actual_availability_error_component import (
        ApiV1BlockRolloutsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_annotations_error_component import (
        ApiV1BlockRolloutsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_archived_at_error_component import (
        ApiV1BlockRolloutsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_archived_error_component import (
        ApiV1BlockRolloutsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_archived_reason_error_component import (
        ApiV1BlockRolloutsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_batch_identifier_error_component import (
        ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_completed_items_error_component import (
        ApiV1BlockRolloutsUpdateCompletedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_conditions_error_component import (
        ApiV1BlockRolloutsUpdateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_criticality_error_component import (
        ApiV1BlockRolloutsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_debug_mode_error_component import (
        ApiV1BlockRolloutsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_discovery_enabled_error_component import (
        ApiV1BlockRolloutsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_discovery_running_error_component import (
        ApiV1BlockRolloutsUpdateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_discovery_task_id_error_component import (
        ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_discovery_task_meta_error_component import (
        ApiV1BlockRolloutsUpdateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_dispatched_items_error_component import (
        ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_display_name_error_component import (
        ApiV1BlockRolloutsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_failed_items_error_component import (
        ApiV1BlockRolloutsUpdateFailedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_kind_error_component import ApiV1BlockRolloutsUpdateKindErrorComponent
    from ..models.api_v1_block_rollouts_update_labels_error_component import (
        ApiV1BlockRolloutsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_last_item_added_at_error_component import (
        ApiV1BlockRolloutsUpdateLastItemAddedAtErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_last_state_change_error_component import (
        ApiV1BlockRolloutsUpdateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_last_state_error_component import (
        ApiV1BlockRolloutsUpdateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_name_error_component import ApiV1BlockRolloutsUpdateNameErrorComponent
    from ..models.api_v1_block_rollouts_update_non_field_errors_error_component import (
        ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_platform_service_error_component import (
        ApiV1BlockRolloutsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_provider_error_component import (
        ApiV1BlockRolloutsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_provider_id_error_component import (
        ApiV1BlockRolloutsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_provider_reference_error_component import (
        ApiV1BlockRolloutsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_quiescence_seconds_error_component import (
        ApiV1BlockRolloutsUpdateQuiescenceSecondsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_reconciliation_running_error_component import (
        ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutsUpdateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutsUpdateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_repair_running_error_component import (
        ApiV1BlockRolloutsUpdateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_repair_task_id_error_component import (
        ApiV1BlockRolloutsUpdateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_repair_task_meta_error_component import (
        ApiV1BlockRolloutsUpdateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_scope_error_component import ApiV1BlockRolloutsUpdateScopeErrorComponent
    from ..models.api_v1_block_rollouts_update_sla_availability_error_component import (
        ApiV1BlockRolloutsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_sla_target_error_component import (
        ApiV1BlockRolloutsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_slo_availability_error_component import (
        ApiV1BlockRolloutsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_slo_target_error_component import (
        ApiV1BlockRolloutsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_state_error_component import ApiV1BlockRolloutsUpdateStateErrorComponent
    from ..models.api_v1_block_rollouts_update_state_reason_error_component import (
        ApiV1BlockRolloutsUpdateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_status_error_component import (
        ApiV1BlockRolloutsUpdateStatusErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_target_availability_error_component import (
        ApiV1BlockRolloutsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_tolerations_error_component import (
        ApiV1BlockRolloutsUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_update_total_items_error_component import (
        ApiV1BlockRolloutsUpdateTotalItemsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutsUpdateValidationError")


@_attrs_define
class ApiV1BlockRolloutsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutsUpdateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutsUpdateAnnotationsErrorComponent | ApiV1BlockRolloutsUpdateArchivedAtErrorComponent |
            ApiV1BlockRolloutsUpdateArchivedErrorComponent | ApiV1BlockRolloutsUpdateArchivedReasonErrorComponent |
            ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponent | ApiV1BlockRolloutsUpdateCompletedItemsErrorComponent |
            ApiV1BlockRolloutsUpdateConditionsErrorComponent | ApiV1BlockRolloutsUpdateCriticalityErrorComponent |
            ApiV1BlockRolloutsUpdateDebugModeErrorComponent | ApiV1BlockRolloutsUpdateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutsUpdateDiscoveryRunningErrorComponent | ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutsUpdateDiscoveryTaskMetaErrorComponent | ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponent
            | ApiV1BlockRolloutsUpdateDisplayNameErrorComponent | ApiV1BlockRolloutsUpdateFailedItemsErrorComponent |
            ApiV1BlockRolloutsUpdateKindErrorComponent | ApiV1BlockRolloutsUpdateLabelsErrorComponent |
            ApiV1BlockRolloutsUpdateLastItemAddedAtErrorComponent | ApiV1BlockRolloutsUpdateLastStateChangeErrorComponent |
            ApiV1BlockRolloutsUpdateLastStateErrorComponent | ApiV1BlockRolloutsUpdateNameErrorComponent |
            ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponent | ApiV1BlockRolloutsUpdatePlatformServiceErrorComponent |
            ApiV1BlockRolloutsUpdateProviderErrorComponent | ApiV1BlockRolloutsUpdateProviderIdErrorComponent |
            ApiV1BlockRolloutsUpdateProviderReferenceErrorComponent |
            ApiV1BlockRolloutsUpdateQuiescenceSecondsErrorComponent |
            ApiV1BlockRolloutsUpdateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutsUpdateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutsUpdateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutsUpdateRepairRunningErrorComponent | ApiV1BlockRolloutsUpdateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutsUpdateRepairTaskMetaErrorComponent | ApiV1BlockRolloutsUpdateScopeErrorComponent |
            ApiV1BlockRolloutsUpdateSlaAvailabilityErrorComponent | ApiV1BlockRolloutsUpdateSlaTargetErrorComponent |
            ApiV1BlockRolloutsUpdateSloAvailabilityErrorComponent | ApiV1BlockRolloutsUpdateSloTargetErrorComponent |
            ApiV1BlockRolloutsUpdateStateErrorComponent | ApiV1BlockRolloutsUpdateStateReasonErrorComponent |
            ApiV1BlockRolloutsUpdateStatusErrorComponent | ApiV1BlockRolloutsUpdateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutsUpdateTolerationsErrorComponent | ApiV1BlockRolloutsUpdateTotalItemsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutsUpdateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutsUpdateAnnotationsErrorComponent
        | ApiV1BlockRolloutsUpdateArchivedAtErrorComponent
        | ApiV1BlockRolloutsUpdateArchivedErrorComponent
        | ApiV1BlockRolloutsUpdateArchivedReasonErrorComponent
        | ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponent
        | ApiV1BlockRolloutsUpdateCompletedItemsErrorComponent
        | ApiV1BlockRolloutsUpdateConditionsErrorComponent
        | ApiV1BlockRolloutsUpdateCriticalityErrorComponent
        | ApiV1BlockRolloutsUpdateDebugModeErrorComponent
        | ApiV1BlockRolloutsUpdateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutsUpdateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutsUpdateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponent
        | ApiV1BlockRolloutsUpdateDisplayNameErrorComponent
        | ApiV1BlockRolloutsUpdateFailedItemsErrorComponent
        | ApiV1BlockRolloutsUpdateKindErrorComponent
        | ApiV1BlockRolloutsUpdateLabelsErrorComponent
        | ApiV1BlockRolloutsUpdateLastItemAddedAtErrorComponent
        | ApiV1BlockRolloutsUpdateLastStateChangeErrorComponent
        | ApiV1BlockRolloutsUpdateLastStateErrorComponent
        | ApiV1BlockRolloutsUpdateNameErrorComponent
        | ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutsUpdatePlatformServiceErrorComponent
        | ApiV1BlockRolloutsUpdateProviderErrorComponent
        | ApiV1BlockRolloutsUpdateProviderIdErrorComponent
        | ApiV1BlockRolloutsUpdateProviderReferenceErrorComponent
        | ApiV1BlockRolloutsUpdateQuiescenceSecondsErrorComponent
        | ApiV1BlockRolloutsUpdateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutsUpdateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutsUpdateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutsUpdateRepairRunningErrorComponent
        | ApiV1BlockRolloutsUpdateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutsUpdateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutsUpdateScopeErrorComponent
        | ApiV1BlockRolloutsUpdateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutsUpdateSlaTargetErrorComponent
        | ApiV1BlockRolloutsUpdateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutsUpdateSloTargetErrorComponent
        | ApiV1BlockRolloutsUpdateStateErrorComponent
        | ApiV1BlockRolloutsUpdateStateReasonErrorComponent
        | ApiV1BlockRolloutsUpdateStatusErrorComponent
        | ApiV1BlockRolloutsUpdateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutsUpdateTolerationsErrorComponent
        | ApiV1BlockRolloutsUpdateTotalItemsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollouts_update_actual_availability_error_component import (
            ApiV1BlockRolloutsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_annotations_error_component import (
            ApiV1BlockRolloutsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_archived_at_error_component import (
            ApiV1BlockRolloutsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_archived_error_component import (
            ApiV1BlockRolloutsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_archived_reason_error_component import (
            ApiV1BlockRolloutsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_batch_identifier_error_component import (
            ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_completed_items_error_component import (
            ApiV1BlockRolloutsUpdateCompletedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_conditions_error_component import (
            ApiV1BlockRolloutsUpdateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_criticality_error_component import (
            ApiV1BlockRolloutsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_debug_mode_error_component import (
            ApiV1BlockRolloutsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_discovery_running_error_component import (
            ApiV1BlockRolloutsUpdateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutsUpdateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_dispatched_items_error_component import (
            ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_display_name_error_component import (
            ApiV1BlockRolloutsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_failed_items_error_component import (
            ApiV1BlockRolloutsUpdateFailedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_kind_error_component import (
            ApiV1BlockRolloutsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_labels_error_component import (
            ApiV1BlockRolloutsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_last_item_added_at_error_component import (
            ApiV1BlockRolloutsUpdateLastItemAddedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_last_state_change_error_component import (
            ApiV1BlockRolloutsUpdateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_last_state_error_component import (
            ApiV1BlockRolloutsUpdateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_name_error_component import (
            ApiV1BlockRolloutsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_non_field_errors_error_component import (
            ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_platform_service_error_component import (
            ApiV1BlockRolloutsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_provider_error_component import (
            ApiV1BlockRolloutsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_provider_id_error_component import (
            ApiV1BlockRolloutsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_provider_reference_error_component import (
            ApiV1BlockRolloutsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutsUpdateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutsUpdateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_repair_running_error_component import (
            ApiV1BlockRolloutsUpdateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_repair_task_id_error_component import (
            ApiV1BlockRolloutsUpdateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutsUpdateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_scope_error_component import (
            ApiV1BlockRolloutsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_sla_availability_error_component import (
            ApiV1BlockRolloutsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_sla_target_error_component import (
            ApiV1BlockRolloutsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_slo_availability_error_component import (
            ApiV1BlockRolloutsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_slo_target_error_component import (
            ApiV1BlockRolloutsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_state_error_component import (
            ApiV1BlockRolloutsUpdateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_state_reason_error_component import (
            ApiV1BlockRolloutsUpdateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_status_error_component import (
            ApiV1BlockRolloutsUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_target_availability_error_component import (
            ApiV1BlockRolloutsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_tolerations_error_component import (
            ApiV1BlockRolloutsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_total_items_error_component import (
            ApiV1BlockRolloutsUpdateTotalItemsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateTotalItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateCompletedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateFailedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsUpdateLastItemAddedAtErrorComponent):
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
        from ..models.api_v1_block_rollouts_update_actual_availability_error_component import (
            ApiV1BlockRolloutsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_annotations_error_component import (
            ApiV1BlockRolloutsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_archived_at_error_component import (
            ApiV1BlockRolloutsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_archived_error_component import (
            ApiV1BlockRolloutsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_archived_reason_error_component import (
            ApiV1BlockRolloutsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_batch_identifier_error_component import (
            ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_completed_items_error_component import (
            ApiV1BlockRolloutsUpdateCompletedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_conditions_error_component import (
            ApiV1BlockRolloutsUpdateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_criticality_error_component import (
            ApiV1BlockRolloutsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_debug_mode_error_component import (
            ApiV1BlockRolloutsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_discovery_running_error_component import (
            ApiV1BlockRolloutsUpdateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutsUpdateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_dispatched_items_error_component import (
            ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_display_name_error_component import (
            ApiV1BlockRolloutsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_failed_items_error_component import (
            ApiV1BlockRolloutsUpdateFailedItemsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_kind_error_component import (
            ApiV1BlockRolloutsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_labels_error_component import (
            ApiV1BlockRolloutsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_last_item_added_at_error_component import (
            ApiV1BlockRolloutsUpdateLastItemAddedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_last_state_change_error_component import (
            ApiV1BlockRolloutsUpdateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_last_state_error_component import (
            ApiV1BlockRolloutsUpdateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_name_error_component import (
            ApiV1BlockRolloutsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_non_field_errors_error_component import (
            ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_platform_service_error_component import (
            ApiV1BlockRolloutsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_provider_error_component import (
            ApiV1BlockRolloutsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_provider_id_error_component import (
            ApiV1BlockRolloutsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_provider_reference_error_component import (
            ApiV1BlockRolloutsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_quiescence_seconds_error_component import (
            ApiV1BlockRolloutsUpdateQuiescenceSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutsUpdateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutsUpdateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_repair_running_error_component import (
            ApiV1BlockRolloutsUpdateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_repair_task_id_error_component import (
            ApiV1BlockRolloutsUpdateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutsUpdateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_scope_error_component import (
            ApiV1BlockRolloutsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_sla_availability_error_component import (
            ApiV1BlockRolloutsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_sla_target_error_component import (
            ApiV1BlockRolloutsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_slo_availability_error_component import (
            ApiV1BlockRolloutsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_slo_target_error_component import (
            ApiV1BlockRolloutsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_state_error_component import (
            ApiV1BlockRolloutsUpdateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_state_reason_error_component import (
            ApiV1BlockRolloutsUpdateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_status_error_component import (
            ApiV1BlockRolloutsUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_target_availability_error_component import (
            ApiV1BlockRolloutsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_tolerations_error_component import (
            ApiV1BlockRolloutsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollouts_update_total_items_error_component import (
            ApiV1BlockRolloutsUpdateTotalItemsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutsUpdateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutsUpdateAnnotationsErrorComponent
                | ApiV1BlockRolloutsUpdateArchivedAtErrorComponent
                | ApiV1BlockRolloutsUpdateArchivedErrorComponent
                | ApiV1BlockRolloutsUpdateArchivedReasonErrorComponent
                | ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponent
                | ApiV1BlockRolloutsUpdateCompletedItemsErrorComponent
                | ApiV1BlockRolloutsUpdateConditionsErrorComponent
                | ApiV1BlockRolloutsUpdateCriticalityErrorComponent
                | ApiV1BlockRolloutsUpdateDebugModeErrorComponent
                | ApiV1BlockRolloutsUpdateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutsUpdateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutsUpdateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponent
                | ApiV1BlockRolloutsUpdateDisplayNameErrorComponent
                | ApiV1BlockRolloutsUpdateFailedItemsErrorComponent
                | ApiV1BlockRolloutsUpdateKindErrorComponent
                | ApiV1BlockRolloutsUpdateLabelsErrorComponent
                | ApiV1BlockRolloutsUpdateLastItemAddedAtErrorComponent
                | ApiV1BlockRolloutsUpdateLastStateChangeErrorComponent
                | ApiV1BlockRolloutsUpdateLastStateErrorComponent
                | ApiV1BlockRolloutsUpdateNameErrorComponent
                | ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutsUpdatePlatformServiceErrorComponent
                | ApiV1BlockRolloutsUpdateProviderErrorComponent
                | ApiV1BlockRolloutsUpdateProviderIdErrorComponent
                | ApiV1BlockRolloutsUpdateProviderReferenceErrorComponent
                | ApiV1BlockRolloutsUpdateQuiescenceSecondsErrorComponent
                | ApiV1BlockRolloutsUpdateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutsUpdateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutsUpdateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutsUpdateRepairRunningErrorComponent
                | ApiV1BlockRolloutsUpdateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutsUpdateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutsUpdateScopeErrorComponent
                | ApiV1BlockRolloutsUpdateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutsUpdateSlaTargetErrorComponent
                | ApiV1BlockRolloutsUpdateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutsUpdateSloTargetErrorComponent
                | ApiV1BlockRolloutsUpdateStateErrorComponent
                | ApiV1BlockRolloutsUpdateStateReasonErrorComponent
                | ApiV1BlockRolloutsUpdateStatusErrorComponent
                | ApiV1BlockRolloutsUpdateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutsUpdateTolerationsErrorComponent
                | ApiV1BlockRolloutsUpdateTotalItemsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_0 = (
                        ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_1 = (
                        ApiV1BlockRolloutsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_2 = (
                        ApiV1BlockRolloutsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_3 = (
                        ApiV1BlockRolloutsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_4 = (
                        ApiV1BlockRolloutsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_5 = (
                        ApiV1BlockRolloutsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_6 = (
                        ApiV1BlockRolloutsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_7 = (
                        ApiV1BlockRolloutsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_8 = (
                        ApiV1BlockRolloutsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_9 = (
                        ApiV1BlockRolloutsUpdateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_10 = (
                        ApiV1BlockRolloutsUpdateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_11 = (
                        ApiV1BlockRolloutsUpdateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_12 = (
                        ApiV1BlockRolloutsUpdateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_13 = (
                        ApiV1BlockRolloutsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_14 = (
                        ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_15 = (
                        ApiV1BlockRolloutsUpdateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_16 = (
                        ApiV1BlockRolloutsUpdateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_17 = (
                        ApiV1BlockRolloutsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_18 = (
                        ApiV1BlockRolloutsUpdateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_19 = (
                        ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_20 = (
                        ApiV1BlockRolloutsUpdateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_21 = (
                        ApiV1BlockRolloutsUpdateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_22 = (
                        ApiV1BlockRolloutsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_23 = (
                        ApiV1BlockRolloutsUpdateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_24 = (
                        ApiV1BlockRolloutsUpdateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_25 = (
                        ApiV1BlockRolloutsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_26 = (
                        ApiV1BlockRolloutsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_27 = (
                        ApiV1BlockRolloutsUpdateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_28 = (
                        ApiV1BlockRolloutsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_29 = (
                        ApiV1BlockRolloutsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_30 = (
                        ApiV1BlockRolloutsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_31 = (
                        ApiV1BlockRolloutsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_32 = (
                        ApiV1BlockRolloutsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_33 = (
                        ApiV1BlockRolloutsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_34 = (
                        ApiV1BlockRolloutsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_35 = (
                        ApiV1BlockRolloutsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_36 = (
                        ApiV1BlockRolloutsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_37 = (
                        ApiV1BlockRolloutsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_38 = (
                        ApiV1BlockRolloutsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_39 = (
                        ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_40 = (
                        ApiV1BlockRolloutsUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_41 = (
                        ApiV1BlockRolloutsUpdateTotalItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_42 = (
                        ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_43 = (
                        ApiV1BlockRolloutsUpdateCompletedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_44 = (
                        ApiV1BlockRolloutsUpdateFailedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_update_error_type_45 = (
                        ApiV1BlockRolloutsUpdateLastItemAddedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollouts_update_error_type_46 = (
                    ApiV1BlockRolloutsUpdateQuiescenceSecondsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollouts_update_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollouts_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollouts_update_validation_error.additional_properties = d
        return api_v1_block_rollouts_update_validation_error

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
