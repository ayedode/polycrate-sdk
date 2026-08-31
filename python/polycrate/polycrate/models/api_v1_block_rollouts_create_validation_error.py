from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollouts_create_actual_availability_error_component import (
        ApiV1BlockRolloutsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_annotations_error_component import (
        ApiV1BlockRolloutsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_archived_at_error_component import (
        ApiV1BlockRolloutsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_archived_error_component import (
        ApiV1BlockRolloutsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_archived_reason_error_component import (
        ApiV1BlockRolloutsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_batch_identifier_error_component import (
        ApiV1BlockRolloutsCreateBatchIdentifierErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_completed_items_error_component import (
        ApiV1BlockRolloutsCreateCompletedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_conditions_error_component import (
        ApiV1BlockRolloutsCreateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_criticality_error_component import (
        ApiV1BlockRolloutsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_debug_mode_error_component import (
        ApiV1BlockRolloutsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_discovery_enabled_error_component import (
        ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_discovery_running_error_component import (
        ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_discovery_task_id_error_component import (
        ApiV1BlockRolloutsCreateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_discovery_task_meta_error_component import (
        ApiV1BlockRolloutsCreateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_dispatched_items_error_component import (
        ApiV1BlockRolloutsCreateDispatchedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_display_name_error_component import (
        ApiV1BlockRolloutsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_failed_items_error_component import (
        ApiV1BlockRolloutsCreateFailedItemsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_kind_error_component import ApiV1BlockRolloutsCreateKindErrorComponent
    from ..models.api_v1_block_rollouts_create_labels_error_component import (
        ApiV1BlockRolloutsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_last_item_added_at_error_component import (
        ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_last_state_change_error_component import (
        ApiV1BlockRolloutsCreateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_last_state_error_component import (
        ApiV1BlockRolloutsCreateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_name_error_component import ApiV1BlockRolloutsCreateNameErrorComponent
    from ..models.api_v1_block_rollouts_create_non_field_errors_error_component import (
        ApiV1BlockRolloutsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_platform_service_error_component import (
        ApiV1BlockRolloutsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_provider_error_component import (
        ApiV1BlockRolloutsCreateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_provider_id_error_component import (
        ApiV1BlockRolloutsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_provider_reference_error_component import (
        ApiV1BlockRolloutsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_quiescence_seconds_error_component import (
        ApiV1BlockRolloutsCreateQuiescenceSecondsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_reconciliation_running_error_component import (
        ApiV1BlockRolloutsCreateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_repair_running_error_component import (
        ApiV1BlockRolloutsCreateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_repair_task_id_error_component import (
        ApiV1BlockRolloutsCreateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_repair_task_meta_error_component import (
        ApiV1BlockRolloutsCreateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_scope_error_component import ApiV1BlockRolloutsCreateScopeErrorComponent
    from ..models.api_v1_block_rollouts_create_sla_availability_error_component import (
        ApiV1BlockRolloutsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_sla_target_error_component import (
        ApiV1BlockRolloutsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_slo_availability_error_component import (
        ApiV1BlockRolloutsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_slo_target_error_component import (
        ApiV1BlockRolloutsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_state_error_component import ApiV1BlockRolloutsCreateStateErrorComponent
    from ..models.api_v1_block_rollouts_create_state_reason_error_component import (
        ApiV1BlockRolloutsCreateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_status_error_component import (
        ApiV1BlockRolloutsCreateStatusErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_target_availability_error_component import (
        ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_tolerations_error_component import (
        ApiV1BlockRolloutsCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_block_rollouts_create_total_items_error_component import (
        ApiV1BlockRolloutsCreateTotalItemsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutsCreateValidationError")


@_attrs_define
class ApiV1BlockRolloutsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutsCreateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutsCreateAnnotationsErrorComponent | ApiV1BlockRolloutsCreateArchivedAtErrorComponent |
            ApiV1BlockRolloutsCreateArchivedErrorComponent | ApiV1BlockRolloutsCreateArchivedReasonErrorComponent |
            ApiV1BlockRolloutsCreateBatchIdentifierErrorComponent | ApiV1BlockRolloutsCreateCompletedItemsErrorComponent |
            ApiV1BlockRolloutsCreateConditionsErrorComponent | ApiV1BlockRolloutsCreateCriticalityErrorComponent |
            ApiV1BlockRolloutsCreateDebugModeErrorComponent | ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponent | ApiV1BlockRolloutsCreateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutsCreateDiscoveryTaskMetaErrorComponent | ApiV1BlockRolloutsCreateDispatchedItemsErrorComponent
            | ApiV1BlockRolloutsCreateDisplayNameErrorComponent | ApiV1BlockRolloutsCreateFailedItemsErrorComponent |
            ApiV1BlockRolloutsCreateKindErrorComponent | ApiV1BlockRolloutsCreateLabelsErrorComponent |
            ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponent | ApiV1BlockRolloutsCreateLastStateChangeErrorComponent |
            ApiV1BlockRolloutsCreateLastStateErrorComponent | ApiV1BlockRolloutsCreateNameErrorComponent |
            ApiV1BlockRolloutsCreateNonFieldErrorsErrorComponent | ApiV1BlockRolloutsCreatePlatformServiceErrorComponent |
            ApiV1BlockRolloutsCreateProviderErrorComponent | ApiV1BlockRolloutsCreateProviderIdErrorComponent |
            ApiV1BlockRolloutsCreateProviderReferenceErrorComponent |
            ApiV1BlockRolloutsCreateQuiescenceSecondsErrorComponent |
            ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutsCreateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutsCreateRepairRunningErrorComponent | ApiV1BlockRolloutsCreateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutsCreateRepairTaskMetaErrorComponent | ApiV1BlockRolloutsCreateScopeErrorComponent |
            ApiV1BlockRolloutsCreateSlaAvailabilityErrorComponent | ApiV1BlockRolloutsCreateSlaTargetErrorComponent |
            ApiV1BlockRolloutsCreateSloAvailabilityErrorComponent | ApiV1BlockRolloutsCreateSloTargetErrorComponent |
            ApiV1BlockRolloutsCreateStateErrorComponent | ApiV1BlockRolloutsCreateStateReasonErrorComponent |
            ApiV1BlockRolloutsCreateStatusErrorComponent | ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutsCreateTolerationsErrorComponent | ApiV1BlockRolloutsCreateTotalItemsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutsCreateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutsCreateAnnotationsErrorComponent
        | ApiV1BlockRolloutsCreateArchivedAtErrorComponent
        | ApiV1BlockRolloutsCreateArchivedErrorComponent
        | ApiV1BlockRolloutsCreateArchivedReasonErrorComponent
        | ApiV1BlockRolloutsCreateBatchIdentifierErrorComponent
        | ApiV1BlockRolloutsCreateCompletedItemsErrorComponent
        | ApiV1BlockRolloutsCreateConditionsErrorComponent
        | ApiV1BlockRolloutsCreateCriticalityErrorComponent
        | ApiV1BlockRolloutsCreateDebugModeErrorComponent
        | ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutsCreateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutsCreateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutsCreateDispatchedItemsErrorComponent
        | ApiV1BlockRolloutsCreateDisplayNameErrorComponent
        | ApiV1BlockRolloutsCreateFailedItemsErrorComponent
        | ApiV1BlockRolloutsCreateKindErrorComponent
        | ApiV1BlockRolloutsCreateLabelsErrorComponent
        | ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponent
        | ApiV1BlockRolloutsCreateLastStateChangeErrorComponent
        | ApiV1BlockRolloutsCreateLastStateErrorComponent
        | ApiV1BlockRolloutsCreateNameErrorComponent
        | ApiV1BlockRolloutsCreateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutsCreatePlatformServiceErrorComponent
        | ApiV1BlockRolloutsCreateProviderErrorComponent
        | ApiV1BlockRolloutsCreateProviderIdErrorComponent
        | ApiV1BlockRolloutsCreateProviderReferenceErrorComponent
        | ApiV1BlockRolloutsCreateQuiescenceSecondsErrorComponent
        | ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutsCreateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutsCreateRepairRunningErrorComponent
        | ApiV1BlockRolloutsCreateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutsCreateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutsCreateScopeErrorComponent
        | ApiV1BlockRolloutsCreateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutsCreateSlaTargetErrorComponent
        | ApiV1BlockRolloutsCreateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutsCreateSloTargetErrorComponent
        | ApiV1BlockRolloutsCreateStateErrorComponent
        | ApiV1BlockRolloutsCreateStateReasonErrorComponent
        | ApiV1BlockRolloutsCreateStatusErrorComponent
        | ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutsCreateTolerationsErrorComponent
        | ApiV1BlockRolloutsCreateTotalItemsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollouts_create_actual_availability_error_component import (
            ApiV1BlockRolloutsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_annotations_error_component import (
            ApiV1BlockRolloutsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_archived_at_error_component import (
            ApiV1BlockRolloutsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_archived_error_component import (
            ApiV1BlockRolloutsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_archived_reason_error_component import (
            ApiV1BlockRolloutsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_batch_identifier_error_component import (
            ApiV1BlockRolloutsCreateBatchIdentifierErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_completed_items_error_component import (
            ApiV1BlockRolloutsCreateCompletedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_conditions_error_component import (
            ApiV1BlockRolloutsCreateConditionsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_criticality_error_component import (
            ApiV1BlockRolloutsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_debug_mode_error_component import (
            ApiV1BlockRolloutsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_discovery_running_error_component import (
            ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutsCreateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutsCreateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_dispatched_items_error_component import (
            ApiV1BlockRolloutsCreateDispatchedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_display_name_error_component import (
            ApiV1BlockRolloutsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_failed_items_error_component import (
            ApiV1BlockRolloutsCreateFailedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_kind_error_component import (
            ApiV1BlockRolloutsCreateKindErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_labels_error_component import (
            ApiV1BlockRolloutsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_last_item_added_at_error_component import (
            ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_last_state_change_error_component import (
            ApiV1BlockRolloutsCreateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_last_state_error_component import (
            ApiV1BlockRolloutsCreateLastStateErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_name_error_component import (
            ApiV1BlockRolloutsCreateNameErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_non_field_errors_error_component import (
            ApiV1BlockRolloutsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_platform_service_error_component import (
            ApiV1BlockRolloutsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_provider_error_component import (
            ApiV1BlockRolloutsCreateProviderErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_provider_id_error_component import (
            ApiV1BlockRolloutsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_provider_reference_error_component import (
            ApiV1BlockRolloutsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutsCreateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_repair_running_error_component import (
            ApiV1BlockRolloutsCreateRepairRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_repair_task_id_error_component import (
            ApiV1BlockRolloutsCreateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutsCreateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_scope_error_component import (
            ApiV1BlockRolloutsCreateScopeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_sla_availability_error_component import (
            ApiV1BlockRolloutsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_sla_target_error_component import (
            ApiV1BlockRolloutsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_slo_availability_error_component import (
            ApiV1BlockRolloutsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_slo_target_error_component import (
            ApiV1BlockRolloutsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_state_error_component import (
            ApiV1BlockRolloutsCreateStateErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_state_reason_error_component import (
            ApiV1BlockRolloutsCreateStateReasonErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_status_error_component import (
            ApiV1BlockRolloutsCreateStatusErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_target_availability_error_component import (
            ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_tolerations_error_component import (
            ApiV1BlockRolloutsCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_total_items_error_component import (
            ApiV1BlockRolloutsCreateTotalItemsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateBatchIdentifierErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateTotalItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateDispatchedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateCompletedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateFailedItemsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponent):
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
        from ..models.api_v1_block_rollouts_create_actual_availability_error_component import (
            ApiV1BlockRolloutsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_annotations_error_component import (
            ApiV1BlockRolloutsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_archived_at_error_component import (
            ApiV1BlockRolloutsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_archived_error_component import (
            ApiV1BlockRolloutsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_archived_reason_error_component import (
            ApiV1BlockRolloutsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_batch_identifier_error_component import (
            ApiV1BlockRolloutsCreateBatchIdentifierErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_completed_items_error_component import (
            ApiV1BlockRolloutsCreateCompletedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_conditions_error_component import (
            ApiV1BlockRolloutsCreateConditionsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_criticality_error_component import (
            ApiV1BlockRolloutsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_debug_mode_error_component import (
            ApiV1BlockRolloutsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_discovery_running_error_component import (
            ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutsCreateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutsCreateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_dispatched_items_error_component import (
            ApiV1BlockRolloutsCreateDispatchedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_display_name_error_component import (
            ApiV1BlockRolloutsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_failed_items_error_component import (
            ApiV1BlockRolloutsCreateFailedItemsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_kind_error_component import (
            ApiV1BlockRolloutsCreateKindErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_labels_error_component import (
            ApiV1BlockRolloutsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_last_item_added_at_error_component import (
            ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_last_state_change_error_component import (
            ApiV1BlockRolloutsCreateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_last_state_error_component import (
            ApiV1BlockRolloutsCreateLastStateErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_name_error_component import (
            ApiV1BlockRolloutsCreateNameErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_non_field_errors_error_component import (
            ApiV1BlockRolloutsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_platform_service_error_component import (
            ApiV1BlockRolloutsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_provider_error_component import (
            ApiV1BlockRolloutsCreateProviderErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_provider_id_error_component import (
            ApiV1BlockRolloutsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_provider_reference_error_component import (
            ApiV1BlockRolloutsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_quiescence_seconds_error_component import (
            ApiV1BlockRolloutsCreateQuiescenceSecondsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutsCreateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_repair_running_error_component import (
            ApiV1BlockRolloutsCreateRepairRunningErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_repair_task_id_error_component import (
            ApiV1BlockRolloutsCreateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutsCreateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_scope_error_component import (
            ApiV1BlockRolloutsCreateScopeErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_sla_availability_error_component import (
            ApiV1BlockRolloutsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_sla_target_error_component import (
            ApiV1BlockRolloutsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_slo_availability_error_component import (
            ApiV1BlockRolloutsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_slo_target_error_component import (
            ApiV1BlockRolloutsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_state_error_component import (
            ApiV1BlockRolloutsCreateStateErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_state_reason_error_component import (
            ApiV1BlockRolloutsCreateStateReasonErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_status_error_component import (
            ApiV1BlockRolloutsCreateStatusErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_target_availability_error_component import (
            ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_tolerations_error_component import (
            ApiV1BlockRolloutsCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_block_rollouts_create_total_items_error_component import (
            ApiV1BlockRolloutsCreateTotalItemsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutsCreateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutsCreateAnnotationsErrorComponent
                | ApiV1BlockRolloutsCreateArchivedAtErrorComponent
                | ApiV1BlockRolloutsCreateArchivedErrorComponent
                | ApiV1BlockRolloutsCreateArchivedReasonErrorComponent
                | ApiV1BlockRolloutsCreateBatchIdentifierErrorComponent
                | ApiV1BlockRolloutsCreateCompletedItemsErrorComponent
                | ApiV1BlockRolloutsCreateConditionsErrorComponent
                | ApiV1BlockRolloutsCreateCriticalityErrorComponent
                | ApiV1BlockRolloutsCreateDebugModeErrorComponent
                | ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutsCreateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutsCreateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutsCreateDispatchedItemsErrorComponent
                | ApiV1BlockRolloutsCreateDisplayNameErrorComponent
                | ApiV1BlockRolloutsCreateFailedItemsErrorComponent
                | ApiV1BlockRolloutsCreateKindErrorComponent
                | ApiV1BlockRolloutsCreateLabelsErrorComponent
                | ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponent
                | ApiV1BlockRolloutsCreateLastStateChangeErrorComponent
                | ApiV1BlockRolloutsCreateLastStateErrorComponent
                | ApiV1BlockRolloutsCreateNameErrorComponent
                | ApiV1BlockRolloutsCreateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutsCreatePlatformServiceErrorComponent
                | ApiV1BlockRolloutsCreateProviderErrorComponent
                | ApiV1BlockRolloutsCreateProviderIdErrorComponent
                | ApiV1BlockRolloutsCreateProviderReferenceErrorComponent
                | ApiV1BlockRolloutsCreateQuiescenceSecondsErrorComponent
                | ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutsCreateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutsCreateRepairRunningErrorComponent
                | ApiV1BlockRolloutsCreateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutsCreateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutsCreateScopeErrorComponent
                | ApiV1BlockRolloutsCreateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutsCreateSlaTargetErrorComponent
                | ApiV1BlockRolloutsCreateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutsCreateSloTargetErrorComponent
                | ApiV1BlockRolloutsCreateStateErrorComponent
                | ApiV1BlockRolloutsCreateStateReasonErrorComponent
                | ApiV1BlockRolloutsCreateStatusErrorComponent
                | ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutsCreateTolerationsErrorComponent
                | ApiV1BlockRolloutsCreateTotalItemsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_0 = (
                        ApiV1BlockRolloutsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_1 = (
                        ApiV1BlockRolloutsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_2 = (
                        ApiV1BlockRolloutsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_3 = (
                        ApiV1BlockRolloutsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_4 = (
                        ApiV1BlockRolloutsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_5 = (
                        ApiV1BlockRolloutsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_6 = (
                        ApiV1BlockRolloutsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_7 = (
                        ApiV1BlockRolloutsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_8 = (
                        ApiV1BlockRolloutsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_9 = (
                        ApiV1BlockRolloutsCreateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_10 = (
                        ApiV1BlockRolloutsCreateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_11 = (
                        ApiV1BlockRolloutsCreateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_12 = (
                        ApiV1BlockRolloutsCreateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_13 = (
                        ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_14 = (
                        ApiV1BlockRolloutsCreateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_15 = (
                        ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_16 = (
                        ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_17 = (
                        ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_18 = (
                        ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_19 = (
                        ApiV1BlockRolloutsCreateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_20 = (
                        ApiV1BlockRolloutsCreateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_21 = (
                        ApiV1BlockRolloutsCreateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_22 = (
                        ApiV1BlockRolloutsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_23 = (
                        ApiV1BlockRolloutsCreateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_24 = (
                        ApiV1BlockRolloutsCreateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_25 = (
                        ApiV1BlockRolloutsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_26 = (
                        ApiV1BlockRolloutsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_27 = (
                        ApiV1BlockRolloutsCreateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_28 = (
                        ApiV1BlockRolloutsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_29 = (
                        ApiV1BlockRolloutsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_30 = (
                        ApiV1BlockRolloutsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_31 = (
                        ApiV1BlockRolloutsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_32 = (
                        ApiV1BlockRolloutsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_33 = (
                        ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_34 = (
                        ApiV1BlockRolloutsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_35 = (
                        ApiV1BlockRolloutsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_36 = (
                        ApiV1BlockRolloutsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_37 = (
                        ApiV1BlockRolloutsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_38 = (
                        ApiV1BlockRolloutsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_39 = (
                        ApiV1BlockRolloutsCreateBatchIdentifierErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_40 = (
                        ApiV1BlockRolloutsCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_41 = (
                        ApiV1BlockRolloutsCreateTotalItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_42 = (
                        ApiV1BlockRolloutsCreateDispatchedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_43 = (
                        ApiV1BlockRolloutsCreateCompletedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_44 = (
                        ApiV1BlockRolloutsCreateFailedItemsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_create_error_type_45 = (
                        ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollouts_create_error_type_46 = (
                    ApiV1BlockRolloutsCreateQuiescenceSecondsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollouts_create_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollouts_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollouts_create_validation_error.additional_properties = d
        return api_v1_block_rollouts_create_validation_error

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
