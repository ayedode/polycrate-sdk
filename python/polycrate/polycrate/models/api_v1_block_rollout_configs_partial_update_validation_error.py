from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollout_configs_partial_update_action_name_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_active_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_actual_availability_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_annotations_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_archived_at_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_archived_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_archived_reason_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_auto_takeover_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_block_config_template_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_block_name_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateBlockNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_bypass_maintenance_window_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_conditions_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_config_to_credential_mappings_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_criticality_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_cron_expression_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateCronExpressionErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_debug_mode_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_discovery_enabled_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_discovery_running_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_discovery_task_id_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_discovery_task_meta_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_display_name_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_enqueue_reason_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateEnqueueReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_failure_threshold_percent_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateFailureThresholdPercentErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_is_system_config_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateIsSystemConfigErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_kind_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_labels_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_last_state_change_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_last_state_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_maintenance_window_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_max_concurrent_percent_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateMaxConcurrentPercentErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_max_retries_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_name_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_non_field_errors_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_notify_on_wave_blocked_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateNotifyOnWaveBlockedErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_platform_service_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_provider_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_provider_id_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_provider_reference_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_running_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_repair_running_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_repair_task_id_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_repair_task_meta_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_scope_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_scope_expressions_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateScopeExpressionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_sla_availability_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_sla_target_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_slo_availability_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_slo_target_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_state_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_state_reason_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_target_availability_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_target_organizations_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateTargetOrganizationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_target_version_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_target_workspaces_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_template_block_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_tolerations_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_partial_update_trigger_type_error_component import (
        ApiV1BlockRolloutConfigsPartialUpdateTriggerTypeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutConfigsPartialUpdateValidationError")


@_attrs_define
class ApiV1BlockRolloutConfigsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateActiveErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateAnnotationsErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateArchivedAtErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateArchivedErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateArchivedReasonErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateBlockNameErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateConditionsErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateCronExpressionErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateDebugModeErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateDisplayNameErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateEnqueueReasonErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateFailureThresholdPercentErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateIsSystemConfigErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateLastStateChangeErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateLastStateErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateMaxConcurrentPercentErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateNameErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateNotifyOnWaveBlockedErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdatePlatformServiceErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateProviderErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateProviderIdErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateProviderReferenceErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateRepairRunningErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateRepairTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateScopeErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateScopeExpressionsErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateSlaTargetErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateStateErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateStateReasonErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateTargetOrganizationsErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateTemplateBlockErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateTolerationsErrorComponent |
            ApiV1BlockRolloutConfigsPartialUpdateTriggerTypeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateActiveErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateAnnotationsErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateArchivedAtErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateArchivedErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateArchivedReasonErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateBlockNameErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateConditionsErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateCronExpressionErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateDebugModeErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateDisplayNameErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateEnqueueReasonErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateFailureThresholdPercentErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateIsSystemConfigErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateLastStateChangeErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateLastStateErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateMaxConcurrentPercentErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateNameErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateNotifyOnWaveBlockedErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdatePlatformServiceErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateProviderErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateProviderIdErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateProviderReferenceErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateRepairRunningErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateScopeErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateScopeExpressionsErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateSlaTargetErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateStateErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateStateReasonErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateTargetOrganizationsErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateTemplateBlockErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateTolerationsErrorComponent
        | ApiV1BlockRolloutConfigsPartialUpdateTriggerTypeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollout_configs_partial_update_action_name_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_active_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_actual_availability_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_annotations_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_archived_at_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_archived_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_archived_reason_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_auto_takeover_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_block_config_template_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_block_name_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateBlockNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_bypass_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_conditions_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateConditionsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_config_to_credential_mappings_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_criticality_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_cron_expression_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateCronExpressionErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_debug_mode_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_discovery_running_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_display_name_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_enqueue_reason_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateEnqueueReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_failure_threshold_percent_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateFailureThresholdPercentErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_is_system_config_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateIsSystemConfigErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_kind_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_labels_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_last_state_change_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_last_state_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateLastStateErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_max_concurrent_percent_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateMaxConcurrentPercentErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_max_retries_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_name_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_non_field_errors_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_platform_service_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_provider_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_provider_id_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_provider_reference_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_repair_running_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateRepairRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_repair_task_id_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_scope_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_scope_expressions_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateScopeExpressionsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_sla_availability_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_sla_target_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_slo_availability_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_slo_target_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_state_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateStateErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_state_reason_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateStateReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_target_availability_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_target_organizations_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTargetOrganizationsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_target_version_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_target_workspaces_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_template_block_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_tolerations_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_trigger_type_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTriggerTypeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateIsSystemConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateTriggerTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateCronExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateEnqueueReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateScopeExpressionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateTargetOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateMaxConcurrentPercentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateFailureThresholdPercentErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponent
            ):
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
        from ..models.api_v1_block_rollout_configs_partial_update_action_name_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_active_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_actual_availability_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_annotations_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_archived_at_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_archived_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_archived_reason_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_auto_takeover_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_block_config_template_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_block_name_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateBlockNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_bypass_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_conditions_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateConditionsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_config_to_credential_mappings_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_criticality_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_cron_expression_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateCronExpressionErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_debug_mode_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_discovery_running_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_display_name_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_enqueue_reason_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateEnqueueReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_failure_threshold_percent_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateFailureThresholdPercentErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_is_system_config_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateIsSystemConfigErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_kind_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_labels_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_last_state_change_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_last_state_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateLastStateErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_max_concurrent_percent_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateMaxConcurrentPercentErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_max_retries_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_name_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_non_field_errors_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_notify_on_wave_blocked_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateNotifyOnWaveBlockedErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_platform_service_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_provider_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_provider_id_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_provider_reference_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_repair_running_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateRepairRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_repair_task_id_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_scope_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_scope_expressions_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateScopeExpressionsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_sla_availability_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_sla_target_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_slo_availability_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_slo_target_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_state_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateStateErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_state_reason_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateStateReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_target_availability_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_target_organizations_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTargetOrganizationsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_target_version_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_target_workspaces_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_template_block_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_tolerations_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_block_rollout_configs_partial_update_trigger_type_error_component import (
            ApiV1BlockRolloutConfigsPartialUpdateTriggerTypeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateActiveErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateAnnotationsErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateArchivedAtErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateArchivedErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateArchivedReasonErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateBlockNameErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateConditionsErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateCronExpressionErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateDebugModeErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateDisplayNameErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateEnqueueReasonErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateFailureThresholdPercentErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateIsSystemConfigErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateLastStateChangeErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateLastStateErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateMaxConcurrentPercentErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateNameErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateNotifyOnWaveBlockedErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdatePlatformServiceErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateProviderErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateProviderIdErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateProviderReferenceErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateRepairRunningErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateScopeErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateScopeExpressionsErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateSlaTargetErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateStateErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateStateReasonErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateTargetOrganizationsErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateTemplateBlockErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateTolerationsErrorComponent
                | ApiV1BlockRolloutConfigsPartialUpdateTriggerTypeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_0 = (
                        ApiV1BlockRolloutConfigsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_1 = (
                        ApiV1BlockRolloutConfigsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_2 = (
                        ApiV1BlockRolloutConfigsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_3 = (
                        ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_4 = (
                        ApiV1BlockRolloutConfigsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_5 = (
                        ApiV1BlockRolloutConfigsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_6 = (
                        ApiV1BlockRolloutConfigsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_7 = (
                        ApiV1BlockRolloutConfigsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_8 = (
                        ApiV1BlockRolloutConfigsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_9 = (
                        ApiV1BlockRolloutConfigsPartialUpdateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_10 = (
                        ApiV1BlockRolloutConfigsPartialUpdateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_11 = (
                        ApiV1BlockRolloutConfigsPartialUpdateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_12 = (
                        ApiV1BlockRolloutConfigsPartialUpdateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_13 = (
                        ApiV1BlockRolloutConfigsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_14 = (
                        ApiV1BlockRolloutConfigsPartialUpdateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_15 = (
                        ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_16 = (
                        ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_17 = (
                        ApiV1BlockRolloutConfigsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_18 = (
                        ApiV1BlockRolloutConfigsPartialUpdateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_19 = (
                        ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_20 = (
                        ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_21 = (
                        ApiV1BlockRolloutConfigsPartialUpdateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_22 = (
                        ApiV1BlockRolloutConfigsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_23 = (
                        ApiV1BlockRolloutConfigsPartialUpdateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_24 = (
                        ApiV1BlockRolloutConfigsPartialUpdateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_25 = (
                        ApiV1BlockRolloutConfigsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_26 = (
                        ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_27 = (
                        ApiV1BlockRolloutConfigsPartialUpdateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_28 = (
                        ApiV1BlockRolloutConfigsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_29 = (
                        ApiV1BlockRolloutConfigsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_30 = (
                        ApiV1BlockRolloutConfigsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_31 = (
                        ApiV1BlockRolloutConfigsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_32 = (
                        ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_33 = (
                        ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_34 = (
                        ApiV1BlockRolloutConfigsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_35 = (
                        ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_36 = (
                        ApiV1BlockRolloutConfigsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_37 = (
                        ApiV1BlockRolloutConfigsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_38 = (
                        ApiV1BlockRolloutConfigsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_39 = (
                        ApiV1BlockRolloutConfigsPartialUpdateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_40 = (
                        ApiV1BlockRolloutConfigsPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_41 = (
                        ApiV1BlockRolloutConfigsPartialUpdateIsSystemConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_42 = (
                        ApiV1BlockRolloutConfigsPartialUpdateTriggerTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_43 = (
                        ApiV1BlockRolloutConfigsPartialUpdateCronExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_44 = (
                        ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_45 = (
                        ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_46 = (
                        ApiV1BlockRolloutConfigsPartialUpdateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_47 = (
                        ApiV1BlockRolloutConfigsPartialUpdateEnqueueReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_48 = (
                        ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_49 = (
                        ApiV1BlockRolloutConfigsPartialUpdateScopeExpressionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_50 = (
                        ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_51 = (
                        ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_52 = (
                        ApiV1BlockRolloutConfigsPartialUpdateTargetOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_53 = (
                        ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_54 = (
                        ApiV1BlockRolloutConfigsPartialUpdateMaxConcurrentPercentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_55 = (
                        ApiV1BlockRolloutConfigsPartialUpdateFailureThresholdPercentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_56 = (
                        ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_57 = (
                        ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_58 = (
                        ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_59 = (
                    ApiV1BlockRolloutConfigsPartialUpdateNotifyOnWaveBlockedErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollout_configs_partial_update_error_type_59

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollout_configs_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollout_configs_partial_update_validation_error.additional_properties = d
        return api_v1_block_rollout_configs_partial_update_validation_error

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
