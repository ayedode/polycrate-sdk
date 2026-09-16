from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollout_configs_update_action_name_error_component import (
        ApiV1BlockRolloutConfigsUpdateActionNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_active_error_component import (
        ApiV1BlockRolloutConfigsUpdateActiveErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_actual_availability_error_component import (
        ApiV1BlockRolloutConfigsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_annotations_error_component import (
        ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_archived_at_error_component import (
        ApiV1BlockRolloutConfigsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_archived_error_component import (
        ApiV1BlockRolloutConfigsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_archived_reason_error_component import (
        ApiV1BlockRolloutConfigsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_auto_takeover_error_component import (
        ApiV1BlockRolloutConfigsUpdateAutoTakeoverErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_block_config_template_error_component import (
        ApiV1BlockRolloutConfigsUpdateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_block_name_error_component import (
        ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_bypass_maintenance_window_error_component import (
        ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_conditions_error_component import (
        ApiV1BlockRolloutConfigsUpdateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_config_to_credential_mappings_error_component import (
        ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_criticality_error_component import (
        ApiV1BlockRolloutConfigsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_cron_expression_error_component import (
        ApiV1BlockRolloutConfigsUpdateCronExpressionErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_debug_mode_error_component import (
        ApiV1BlockRolloutConfigsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_discovery_enabled_error_component import (
        ApiV1BlockRolloutConfigsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_discovery_running_error_component import (
        ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_discovery_task_id_error_component import (
        ApiV1BlockRolloutConfigsUpdateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_discovery_task_meta_error_component import (
        ApiV1BlockRolloutConfigsUpdateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_display_name_error_component import (
        ApiV1BlockRolloutConfigsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_enqueue_reason_error_component import (
        ApiV1BlockRolloutConfigsUpdateEnqueueReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_failure_threshold_percent_error_component import (
        ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_is_system_config_error_component import (
        ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_kind_error_component import (
        ApiV1BlockRolloutConfigsUpdateKindErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_labels_error_component import (
        ApiV1BlockRolloutConfigsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_last_state_change_error_component import (
        ApiV1BlockRolloutConfigsUpdateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_last_state_error_component import (
        ApiV1BlockRolloutConfigsUpdateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_maintenance_window_error_component import (
        ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_max_concurrent_percent_error_component import (
        ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_max_retries_error_component import (
        ApiV1BlockRolloutConfigsUpdateMaxRetriesErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_name_error_component import (
        ApiV1BlockRolloutConfigsUpdateNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_non_field_errors_error_component import (
        ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_notify_on_wave_blocked_error_component import (
        ApiV1BlockRolloutConfigsUpdateNotifyOnWaveBlockedErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_platform_service_error_component import (
        ApiV1BlockRolloutConfigsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_provider_error_component import (
        ApiV1BlockRolloutConfigsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_provider_id_error_component import (
        ApiV1BlockRolloutConfigsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_provider_reference_error_component import (
        ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutConfigsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_reconciliation_running_error_component import (
        ApiV1BlockRolloutConfigsUpdateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutConfigsUpdateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutConfigsUpdateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_repair_running_error_component import (
        ApiV1BlockRolloutConfigsUpdateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_repair_task_id_error_component import (
        ApiV1BlockRolloutConfigsUpdateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_repair_task_meta_error_component import (
        ApiV1BlockRolloutConfigsUpdateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_scope_error_component import (
        ApiV1BlockRolloutConfigsUpdateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_scope_expressions_error_component import (
        ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_sla_availability_error_component import (
        ApiV1BlockRolloutConfigsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_sla_target_error_component import (
        ApiV1BlockRolloutConfigsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_slo_availability_error_component import (
        ApiV1BlockRolloutConfigsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_slo_target_error_component import (
        ApiV1BlockRolloutConfigsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_state_error_component import (
        ApiV1BlockRolloutConfigsUpdateStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_state_reason_error_component import (
        ApiV1BlockRolloutConfigsUpdateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_target_availability_error_component import (
        ApiV1BlockRolloutConfigsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_target_organizations_error_component import (
        ApiV1BlockRolloutConfigsUpdateTargetOrganizationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_target_version_error_component import (
        ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_target_workspaces_error_component import (
        ApiV1BlockRolloutConfigsUpdateTargetWorkspacesErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_template_block_error_component import (
        ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_tolerations_error_component import (
        ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_update_trigger_type_error_component import (
        ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutConfigsUpdateValidationError")


@_attrs_define
class ApiV1BlockRolloutConfigsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutConfigsUpdateActionNameErrorComponent |
            ApiV1BlockRolloutConfigsUpdateActiveErrorComponent |
            ApiV1BlockRolloutConfigsUpdateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponent | ApiV1BlockRolloutConfigsUpdateArchivedAtErrorComponent
            | ApiV1BlockRolloutConfigsUpdateArchivedErrorComponent |
            ApiV1BlockRolloutConfigsUpdateArchivedReasonErrorComponent |
            ApiV1BlockRolloutConfigsUpdateAutoTakeoverErrorComponent |
            ApiV1BlockRolloutConfigsUpdateBlockConfigTemplateErrorComponent |
            ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponent |
            ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponent |
            ApiV1BlockRolloutConfigsUpdateConditionsErrorComponent |
            ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponent |
            ApiV1BlockRolloutConfigsUpdateCriticalityErrorComponent |
            ApiV1BlockRolloutConfigsUpdateCronExpressionErrorComponent |
            ApiV1BlockRolloutConfigsUpdateDebugModeErrorComponent |
            ApiV1BlockRolloutConfigsUpdateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutConfigsUpdateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsUpdateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsUpdateDisplayNameErrorComponent |
            ApiV1BlockRolloutConfigsUpdateEnqueueReasonErrorComponent |
            ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponent |
            ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponent | ApiV1BlockRolloutConfigsUpdateKindErrorComponent |
            ApiV1BlockRolloutConfigsUpdateLabelsErrorComponent | ApiV1BlockRolloutConfigsUpdateLastStateChangeErrorComponent
            | ApiV1BlockRolloutConfigsUpdateLastStateErrorComponent |
            ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponent |
            ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponent |
            ApiV1BlockRolloutConfigsUpdateMaxRetriesErrorComponent | ApiV1BlockRolloutConfigsUpdateNameErrorComponent |
            ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutConfigsUpdateNotifyOnWaveBlockedErrorComponent |
            ApiV1BlockRolloutConfigsUpdatePlatformServiceErrorComponent |
            ApiV1BlockRolloutConfigsUpdateProviderErrorComponent | ApiV1BlockRolloutConfigsUpdateProviderIdErrorComponent |
            ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponent |
            ApiV1BlockRolloutConfigsUpdateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutConfigsUpdateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutConfigsUpdateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsUpdateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsUpdateRepairRunningErrorComponent |
            ApiV1BlockRolloutConfigsUpdateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsUpdateRepairTaskMetaErrorComponent | ApiV1BlockRolloutConfigsUpdateScopeErrorComponent |
            ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponent |
            ApiV1BlockRolloutConfigsUpdateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsUpdateSlaTargetErrorComponent |
            ApiV1BlockRolloutConfigsUpdateSloAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsUpdateSloTargetErrorComponent | ApiV1BlockRolloutConfigsUpdateStateErrorComponent |
            ApiV1BlockRolloutConfigsUpdateStateReasonErrorComponent |
            ApiV1BlockRolloutConfigsUpdateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsUpdateTargetOrganizationsErrorComponent |
            ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponent |
            ApiV1BlockRolloutConfigsUpdateTargetWorkspacesErrorComponent |
            ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponent |
            ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponent |
            ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutConfigsUpdateActionNameErrorComponent
        | ApiV1BlockRolloutConfigsUpdateActiveErrorComponent
        | ApiV1BlockRolloutConfigsUpdateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponent
        | ApiV1BlockRolloutConfigsUpdateArchivedAtErrorComponent
        | ApiV1BlockRolloutConfigsUpdateArchivedErrorComponent
        | ApiV1BlockRolloutConfigsUpdateArchivedReasonErrorComponent
        | ApiV1BlockRolloutConfigsUpdateAutoTakeoverErrorComponent
        | ApiV1BlockRolloutConfigsUpdateBlockConfigTemplateErrorComponent
        | ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponent
        | ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponent
        | ApiV1BlockRolloutConfigsUpdateConditionsErrorComponent
        | ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponent
        | ApiV1BlockRolloutConfigsUpdateCriticalityErrorComponent
        | ApiV1BlockRolloutConfigsUpdateCronExpressionErrorComponent
        | ApiV1BlockRolloutConfigsUpdateDebugModeErrorComponent
        | ApiV1BlockRolloutConfigsUpdateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutConfigsUpdateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsUpdateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsUpdateDisplayNameErrorComponent
        | ApiV1BlockRolloutConfigsUpdateEnqueueReasonErrorComponent
        | ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponent
        | ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponent
        | ApiV1BlockRolloutConfigsUpdateKindErrorComponent
        | ApiV1BlockRolloutConfigsUpdateLabelsErrorComponent
        | ApiV1BlockRolloutConfigsUpdateLastStateChangeErrorComponent
        | ApiV1BlockRolloutConfigsUpdateLastStateErrorComponent
        | ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponent
        | ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponent
        | ApiV1BlockRolloutConfigsUpdateMaxRetriesErrorComponent
        | ApiV1BlockRolloutConfigsUpdateNameErrorComponent
        | ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutConfigsUpdateNotifyOnWaveBlockedErrorComponent
        | ApiV1BlockRolloutConfigsUpdatePlatformServiceErrorComponent
        | ApiV1BlockRolloutConfigsUpdateProviderErrorComponent
        | ApiV1BlockRolloutConfigsUpdateProviderIdErrorComponent
        | ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponent
        | ApiV1BlockRolloutConfigsUpdateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutConfigsUpdateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutConfigsUpdateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsUpdateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsUpdateRepairRunningErrorComponent
        | ApiV1BlockRolloutConfigsUpdateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsUpdateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsUpdateScopeErrorComponent
        | ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponent
        | ApiV1BlockRolloutConfigsUpdateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsUpdateSlaTargetErrorComponent
        | ApiV1BlockRolloutConfigsUpdateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsUpdateSloTargetErrorComponent
        | ApiV1BlockRolloutConfigsUpdateStateErrorComponent
        | ApiV1BlockRolloutConfigsUpdateStateReasonErrorComponent
        | ApiV1BlockRolloutConfigsUpdateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsUpdateTargetOrganizationsErrorComponent
        | ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponent
        | ApiV1BlockRolloutConfigsUpdateTargetWorkspacesErrorComponent
        | ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponent
        | ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponent
        | ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollout_configs_update_action_name_error_component import (
            ApiV1BlockRolloutConfigsUpdateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_active_error_component import (
            ApiV1BlockRolloutConfigsUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_actual_availability_error_component import (
            ApiV1BlockRolloutConfigsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_annotations_error_component import (
            ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_archived_at_error_component import (
            ApiV1BlockRolloutConfigsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_archived_error_component import (
            ApiV1BlockRolloutConfigsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_archived_reason_error_component import (
            ApiV1BlockRolloutConfigsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_auto_takeover_error_component import (
            ApiV1BlockRolloutConfigsUpdateAutoTakeoverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_block_config_template_error_component import (
            ApiV1BlockRolloutConfigsUpdateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_block_name_error_component import (
            ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_bypass_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_conditions_error_component import (
            ApiV1BlockRolloutConfigsUpdateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_config_to_credential_mappings_error_component import (
            ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_criticality_error_component import (
            ApiV1BlockRolloutConfigsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_cron_expression_error_component import (
            ApiV1BlockRolloutConfigsUpdateCronExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_debug_mode_error_component import (
            ApiV1BlockRolloutConfigsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutConfigsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_discovery_running_error_component import (
            ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutConfigsUpdateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutConfigsUpdateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_display_name_error_component import (
            ApiV1BlockRolloutConfigsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_enqueue_reason_error_component import (
            ApiV1BlockRolloutConfigsUpdateEnqueueReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_failure_threshold_percent_error_component import (
            ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_is_system_config_error_component import (
            ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_kind_error_component import (
            ApiV1BlockRolloutConfigsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_labels_error_component import (
            ApiV1BlockRolloutConfigsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_last_state_change_error_component import (
            ApiV1BlockRolloutConfigsUpdateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_last_state_error_component import (
            ApiV1BlockRolloutConfigsUpdateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_max_concurrent_percent_error_component import (
            ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_max_retries_error_component import (
            ApiV1BlockRolloutConfigsUpdateMaxRetriesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_name_error_component import (
            ApiV1BlockRolloutConfigsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_non_field_errors_error_component import (
            ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_platform_service_error_component import (
            ApiV1BlockRolloutConfigsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_provider_error_component import (
            ApiV1BlockRolloutConfigsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_provider_id_error_component import (
            ApiV1BlockRolloutConfigsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_provider_reference_error_component import (
            ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutConfigsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutConfigsUpdateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutConfigsUpdateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutConfigsUpdateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_repair_running_error_component import (
            ApiV1BlockRolloutConfigsUpdateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_repair_task_id_error_component import (
            ApiV1BlockRolloutConfigsUpdateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutConfigsUpdateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_scope_error_component import (
            ApiV1BlockRolloutConfigsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_scope_expressions_error_component import (
            ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_sla_availability_error_component import (
            ApiV1BlockRolloutConfigsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_sla_target_error_component import (
            ApiV1BlockRolloutConfigsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_slo_availability_error_component import (
            ApiV1BlockRolloutConfigsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_slo_target_error_component import (
            ApiV1BlockRolloutConfigsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_state_error_component import (
            ApiV1BlockRolloutConfigsUpdateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_state_reason_error_component import (
            ApiV1BlockRolloutConfigsUpdateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_target_availability_error_component import (
            ApiV1BlockRolloutConfigsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_target_organizations_error_component import (
            ApiV1BlockRolloutConfigsUpdateTargetOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_target_version_error_component import (
            ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_target_workspaces_error_component import (
            ApiV1BlockRolloutConfigsUpdateTargetWorkspacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_template_block_error_component import (
            ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_tolerations_error_component import (
            ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_trigger_type_error_component import (
            ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateCronExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateActionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateEnqueueReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateBlockConfigTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateAutoTakeoverErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateTargetOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateTargetWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateMaxRetriesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponent):
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
        from ..models.api_v1_block_rollout_configs_update_action_name_error_component import (
            ApiV1BlockRolloutConfigsUpdateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_active_error_component import (
            ApiV1BlockRolloutConfigsUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_actual_availability_error_component import (
            ApiV1BlockRolloutConfigsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_annotations_error_component import (
            ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_archived_at_error_component import (
            ApiV1BlockRolloutConfigsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_archived_error_component import (
            ApiV1BlockRolloutConfigsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_archived_reason_error_component import (
            ApiV1BlockRolloutConfigsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_auto_takeover_error_component import (
            ApiV1BlockRolloutConfigsUpdateAutoTakeoverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_block_config_template_error_component import (
            ApiV1BlockRolloutConfigsUpdateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_block_name_error_component import (
            ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_bypass_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_conditions_error_component import (
            ApiV1BlockRolloutConfigsUpdateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_config_to_credential_mappings_error_component import (
            ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_criticality_error_component import (
            ApiV1BlockRolloutConfigsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_cron_expression_error_component import (
            ApiV1BlockRolloutConfigsUpdateCronExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_debug_mode_error_component import (
            ApiV1BlockRolloutConfigsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutConfigsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_discovery_running_error_component import (
            ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutConfigsUpdateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutConfigsUpdateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_display_name_error_component import (
            ApiV1BlockRolloutConfigsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_enqueue_reason_error_component import (
            ApiV1BlockRolloutConfigsUpdateEnqueueReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_failure_threshold_percent_error_component import (
            ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_is_system_config_error_component import (
            ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_kind_error_component import (
            ApiV1BlockRolloutConfigsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_labels_error_component import (
            ApiV1BlockRolloutConfigsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_last_state_change_error_component import (
            ApiV1BlockRolloutConfigsUpdateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_last_state_error_component import (
            ApiV1BlockRolloutConfigsUpdateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_max_concurrent_percent_error_component import (
            ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_max_retries_error_component import (
            ApiV1BlockRolloutConfigsUpdateMaxRetriesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_name_error_component import (
            ApiV1BlockRolloutConfigsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_non_field_errors_error_component import (
            ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_notify_on_wave_blocked_error_component import (
            ApiV1BlockRolloutConfigsUpdateNotifyOnWaveBlockedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_platform_service_error_component import (
            ApiV1BlockRolloutConfigsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_provider_error_component import (
            ApiV1BlockRolloutConfigsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_provider_id_error_component import (
            ApiV1BlockRolloutConfigsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_provider_reference_error_component import (
            ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutConfigsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutConfigsUpdateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutConfigsUpdateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutConfigsUpdateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_repair_running_error_component import (
            ApiV1BlockRolloutConfigsUpdateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_repair_task_id_error_component import (
            ApiV1BlockRolloutConfigsUpdateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutConfigsUpdateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_scope_error_component import (
            ApiV1BlockRolloutConfigsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_scope_expressions_error_component import (
            ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_sla_availability_error_component import (
            ApiV1BlockRolloutConfigsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_sla_target_error_component import (
            ApiV1BlockRolloutConfigsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_slo_availability_error_component import (
            ApiV1BlockRolloutConfigsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_slo_target_error_component import (
            ApiV1BlockRolloutConfigsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_state_error_component import (
            ApiV1BlockRolloutConfigsUpdateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_state_reason_error_component import (
            ApiV1BlockRolloutConfigsUpdateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_target_availability_error_component import (
            ApiV1BlockRolloutConfigsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_target_organizations_error_component import (
            ApiV1BlockRolloutConfigsUpdateTargetOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_target_version_error_component import (
            ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_target_workspaces_error_component import (
            ApiV1BlockRolloutConfigsUpdateTargetWorkspacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_template_block_error_component import (
            ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_tolerations_error_component import (
            ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_update_trigger_type_error_component import (
            ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutConfigsUpdateActionNameErrorComponent
                | ApiV1BlockRolloutConfigsUpdateActiveErrorComponent
                | ApiV1BlockRolloutConfigsUpdateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponent
                | ApiV1BlockRolloutConfigsUpdateArchivedAtErrorComponent
                | ApiV1BlockRolloutConfigsUpdateArchivedErrorComponent
                | ApiV1BlockRolloutConfigsUpdateArchivedReasonErrorComponent
                | ApiV1BlockRolloutConfigsUpdateAutoTakeoverErrorComponent
                | ApiV1BlockRolloutConfigsUpdateBlockConfigTemplateErrorComponent
                | ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponent
                | ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponent
                | ApiV1BlockRolloutConfigsUpdateConditionsErrorComponent
                | ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponent
                | ApiV1BlockRolloutConfigsUpdateCriticalityErrorComponent
                | ApiV1BlockRolloutConfigsUpdateCronExpressionErrorComponent
                | ApiV1BlockRolloutConfigsUpdateDebugModeErrorComponent
                | ApiV1BlockRolloutConfigsUpdateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutConfigsUpdateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsUpdateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsUpdateDisplayNameErrorComponent
                | ApiV1BlockRolloutConfigsUpdateEnqueueReasonErrorComponent
                | ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponent
                | ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponent
                | ApiV1BlockRolloutConfigsUpdateKindErrorComponent
                | ApiV1BlockRolloutConfigsUpdateLabelsErrorComponent
                | ApiV1BlockRolloutConfigsUpdateLastStateChangeErrorComponent
                | ApiV1BlockRolloutConfigsUpdateLastStateErrorComponent
                | ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponent
                | ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponent
                | ApiV1BlockRolloutConfigsUpdateMaxRetriesErrorComponent
                | ApiV1BlockRolloutConfigsUpdateNameErrorComponent
                | ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutConfigsUpdateNotifyOnWaveBlockedErrorComponent
                | ApiV1BlockRolloutConfigsUpdatePlatformServiceErrorComponent
                | ApiV1BlockRolloutConfigsUpdateProviderErrorComponent
                | ApiV1BlockRolloutConfigsUpdateProviderIdErrorComponent
                | ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponent
                | ApiV1BlockRolloutConfigsUpdateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutConfigsUpdateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutConfigsUpdateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsUpdateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsUpdateRepairRunningErrorComponent
                | ApiV1BlockRolloutConfigsUpdateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsUpdateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsUpdateScopeErrorComponent
                | ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponent
                | ApiV1BlockRolloutConfigsUpdateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsUpdateSlaTargetErrorComponent
                | ApiV1BlockRolloutConfigsUpdateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsUpdateSloTargetErrorComponent
                | ApiV1BlockRolloutConfigsUpdateStateErrorComponent
                | ApiV1BlockRolloutConfigsUpdateStateReasonErrorComponent
                | ApiV1BlockRolloutConfigsUpdateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsUpdateTargetOrganizationsErrorComponent
                | ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponent
                | ApiV1BlockRolloutConfigsUpdateTargetWorkspacesErrorComponent
                | ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponent
                | ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponent
                | ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_0 = (
                        ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_1 = (
                        ApiV1BlockRolloutConfigsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_2 = (
                        ApiV1BlockRolloutConfigsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_3 = (
                        ApiV1BlockRolloutConfigsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_4 = (
                        ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_5 = (
                        ApiV1BlockRolloutConfigsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_6 = (
                        ApiV1BlockRolloutConfigsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_7 = (
                        ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_8 = (
                        ApiV1BlockRolloutConfigsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_9 = (
                        ApiV1BlockRolloutConfigsUpdateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_10 = (
                        ApiV1BlockRolloutConfigsUpdateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_11 = (
                        ApiV1BlockRolloutConfigsUpdateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_12 = (
                        ApiV1BlockRolloutConfigsUpdateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_13 = (
                        ApiV1BlockRolloutConfigsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_14 = (
                        ApiV1BlockRolloutConfigsUpdateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_15 = (
                        ApiV1BlockRolloutConfigsUpdateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_16 = (
                        ApiV1BlockRolloutConfigsUpdateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_17 = (
                        ApiV1BlockRolloutConfigsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_18 = (
                        ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_19 = (
                        ApiV1BlockRolloutConfigsUpdateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_20 = (
                        ApiV1BlockRolloutConfigsUpdateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_21 = (
                        ApiV1BlockRolloutConfigsUpdateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_22 = (
                        ApiV1BlockRolloutConfigsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_23 = (
                        ApiV1BlockRolloutConfigsUpdateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_24 = (
                        ApiV1BlockRolloutConfigsUpdateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_25 = (
                        ApiV1BlockRolloutConfigsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_26 = (
                        ApiV1BlockRolloutConfigsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_27 = (
                        ApiV1BlockRolloutConfigsUpdateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_28 = (
                        ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_29 = (
                        ApiV1BlockRolloutConfigsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_30 = (
                        ApiV1BlockRolloutConfigsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_31 = (
                        ApiV1BlockRolloutConfigsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_32 = (
                        ApiV1BlockRolloutConfigsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_33 = (
                        ApiV1BlockRolloutConfigsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_34 = (
                        ApiV1BlockRolloutConfigsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_35 = (
                        ApiV1BlockRolloutConfigsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_36 = (
                        ApiV1BlockRolloutConfigsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_37 = (
                        ApiV1BlockRolloutConfigsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_38 = (
                        ApiV1BlockRolloutConfigsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_39 = (
                        ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_40 = (
                        ApiV1BlockRolloutConfigsUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_41 = (
                        ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_42 = (
                        ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_43 = (
                        ApiV1BlockRolloutConfigsUpdateCronExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_44 = (
                        ApiV1BlockRolloutConfigsUpdateActionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_45 = (
                        ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_46 = (
                        ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_47 = (
                        ApiV1BlockRolloutConfigsUpdateEnqueueReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_48 = (
                        ApiV1BlockRolloutConfigsUpdateBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_49 = (
                        ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_50 = (
                        ApiV1BlockRolloutConfigsUpdateAutoTakeoverErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_51 = (
                        ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_52 = (
                        ApiV1BlockRolloutConfigsUpdateTargetOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_53 = (
                        ApiV1BlockRolloutConfigsUpdateTargetWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_54 = (
                        ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_55 = (
                        ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_56 = (
                        ApiV1BlockRolloutConfigsUpdateMaxRetriesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_57 = (
                        ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_update_error_type_58 = (
                        ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_update_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollout_configs_update_error_type_59 = (
                    ApiV1BlockRolloutConfigsUpdateNotifyOnWaveBlockedErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollout_configs_update_error_type_59

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollout_configs_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollout_configs_update_validation_error.additional_properties = d
        return api_v1_block_rollout_configs_update_validation_error

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
