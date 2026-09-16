from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollout_configs_create_action_name_error_component import (
        ApiV1BlockRolloutConfigsCreateActionNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_active_error_component import (
        ApiV1BlockRolloutConfigsCreateActiveErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_actual_availability_error_component import (
        ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_annotations_error_component import (
        ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_archived_at_error_component import (
        ApiV1BlockRolloutConfigsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_archived_error_component import (
        ApiV1BlockRolloutConfigsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_archived_reason_error_component import (
        ApiV1BlockRolloutConfigsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_auto_takeover_error_component import (
        ApiV1BlockRolloutConfigsCreateAutoTakeoverErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_block_config_template_error_component import (
        ApiV1BlockRolloutConfigsCreateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_block_name_error_component import (
        ApiV1BlockRolloutConfigsCreateBlockNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_bypass_maintenance_window_error_component import (
        ApiV1BlockRolloutConfigsCreateBypassMaintenanceWindowErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_conditions_error_component import (
        ApiV1BlockRolloutConfigsCreateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_config_to_credential_mappings_error_component import (
        ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_criticality_error_component import (
        ApiV1BlockRolloutConfigsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_cron_expression_error_component import (
        ApiV1BlockRolloutConfigsCreateCronExpressionErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_debug_mode_error_component import (
        ApiV1BlockRolloutConfigsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_discovery_enabled_error_component import (
        ApiV1BlockRolloutConfigsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_discovery_running_error_component import (
        ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_discovery_task_id_error_component import (
        ApiV1BlockRolloutConfigsCreateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_discovery_task_meta_error_component import (
        ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_display_name_error_component import (
        ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_enqueue_reason_error_component import (
        ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_failure_threshold_percent_error_component import (
        ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_is_system_config_error_component import (
        ApiV1BlockRolloutConfigsCreateIsSystemConfigErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_kind_error_component import (
        ApiV1BlockRolloutConfigsCreateKindErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_labels_error_component import (
        ApiV1BlockRolloutConfigsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_last_state_change_error_component import (
        ApiV1BlockRolloutConfigsCreateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_last_state_error_component import (
        ApiV1BlockRolloutConfigsCreateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_maintenance_window_error_component import (
        ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_max_concurrent_percent_error_component import (
        ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_max_retries_error_component import (
        ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_name_error_component import (
        ApiV1BlockRolloutConfigsCreateNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_non_field_errors_error_component import (
        ApiV1BlockRolloutConfigsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_notify_on_wave_blocked_error_component import (
        ApiV1BlockRolloutConfigsCreateNotifyOnWaveBlockedErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_platform_service_error_component import (
        ApiV1BlockRolloutConfigsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_provider_error_component import (
        ApiV1BlockRolloutConfigsCreateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_provider_id_error_component import (
        ApiV1BlockRolloutConfigsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_provider_reference_error_component import (
        ApiV1BlockRolloutConfigsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutConfigsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_reconciliation_running_error_component import (
        ApiV1BlockRolloutConfigsCreateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutConfigsCreateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutConfigsCreateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_repair_running_error_component import (
        ApiV1BlockRolloutConfigsCreateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_repair_task_id_error_component import (
        ApiV1BlockRolloutConfigsCreateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_repair_task_meta_error_component import (
        ApiV1BlockRolloutConfigsCreateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_scope_error_component import (
        ApiV1BlockRolloutConfigsCreateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_scope_expressions_error_component import (
        ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_sla_availability_error_component import (
        ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_sla_target_error_component import (
        ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_slo_availability_error_component import (
        ApiV1BlockRolloutConfigsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_slo_target_error_component import (
        ApiV1BlockRolloutConfigsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_state_error_component import (
        ApiV1BlockRolloutConfigsCreateStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_state_reason_error_component import (
        ApiV1BlockRolloutConfigsCreateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_target_availability_error_component import (
        ApiV1BlockRolloutConfigsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_target_organizations_error_component import (
        ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_target_version_error_component import (
        ApiV1BlockRolloutConfigsCreateTargetVersionErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_target_workspaces_error_component import (
        ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_template_block_error_component import (
        ApiV1BlockRolloutConfigsCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_tolerations_error_component import (
        ApiV1BlockRolloutConfigsCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_create_trigger_type_error_component import (
        ApiV1BlockRolloutConfigsCreateTriggerTypeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutConfigsCreateValidationError")


@_attrs_define
class ApiV1BlockRolloutConfigsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutConfigsCreateActionNameErrorComponent |
            ApiV1BlockRolloutConfigsCreateActiveErrorComponent |
            ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponent | ApiV1BlockRolloutConfigsCreateArchivedAtErrorComponent
            | ApiV1BlockRolloutConfigsCreateArchivedErrorComponent |
            ApiV1BlockRolloutConfigsCreateArchivedReasonErrorComponent |
            ApiV1BlockRolloutConfigsCreateAutoTakeoverErrorComponent |
            ApiV1BlockRolloutConfigsCreateBlockConfigTemplateErrorComponent |
            ApiV1BlockRolloutConfigsCreateBlockNameErrorComponent |
            ApiV1BlockRolloutConfigsCreateBypassMaintenanceWindowErrorComponent |
            ApiV1BlockRolloutConfigsCreateConditionsErrorComponent |
            ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponent |
            ApiV1BlockRolloutConfigsCreateCriticalityErrorComponent |
            ApiV1BlockRolloutConfigsCreateCronExpressionErrorComponent |
            ApiV1BlockRolloutConfigsCreateDebugModeErrorComponent |
            ApiV1BlockRolloutConfigsCreateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutConfigsCreateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponent |
            ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponent |
            ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponent |
            ApiV1BlockRolloutConfigsCreateIsSystemConfigErrorComponent | ApiV1BlockRolloutConfigsCreateKindErrorComponent |
            ApiV1BlockRolloutConfigsCreateLabelsErrorComponent | ApiV1BlockRolloutConfigsCreateLastStateChangeErrorComponent
            | ApiV1BlockRolloutConfigsCreateLastStateErrorComponent |
            ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponent |
            ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponent |
            ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponent | ApiV1BlockRolloutConfigsCreateNameErrorComponent |
            ApiV1BlockRolloutConfigsCreateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutConfigsCreateNotifyOnWaveBlockedErrorComponent |
            ApiV1BlockRolloutConfigsCreatePlatformServiceErrorComponent |
            ApiV1BlockRolloutConfigsCreateProviderErrorComponent | ApiV1BlockRolloutConfigsCreateProviderIdErrorComponent |
            ApiV1BlockRolloutConfigsCreateProviderReferenceErrorComponent |
            ApiV1BlockRolloutConfigsCreateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutConfigsCreateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutConfigsCreateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsCreateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsCreateRepairRunningErrorComponent |
            ApiV1BlockRolloutConfigsCreateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsCreateRepairTaskMetaErrorComponent | ApiV1BlockRolloutConfigsCreateScopeErrorComponent |
            ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponent |
            ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponent |
            ApiV1BlockRolloutConfigsCreateSloAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsCreateSloTargetErrorComponent | ApiV1BlockRolloutConfigsCreateStateErrorComponent |
            ApiV1BlockRolloutConfigsCreateStateReasonErrorComponent |
            ApiV1BlockRolloutConfigsCreateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponent |
            ApiV1BlockRolloutConfigsCreateTargetVersionErrorComponent |
            ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponent |
            ApiV1BlockRolloutConfigsCreateTemplateBlockErrorComponent |
            ApiV1BlockRolloutConfigsCreateTolerationsErrorComponent |
            ApiV1BlockRolloutConfigsCreateTriggerTypeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutConfigsCreateActionNameErrorComponent
        | ApiV1BlockRolloutConfigsCreateActiveErrorComponent
        | ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponent
        | ApiV1BlockRolloutConfigsCreateArchivedAtErrorComponent
        | ApiV1BlockRolloutConfigsCreateArchivedErrorComponent
        | ApiV1BlockRolloutConfigsCreateArchivedReasonErrorComponent
        | ApiV1BlockRolloutConfigsCreateAutoTakeoverErrorComponent
        | ApiV1BlockRolloutConfigsCreateBlockConfigTemplateErrorComponent
        | ApiV1BlockRolloutConfigsCreateBlockNameErrorComponent
        | ApiV1BlockRolloutConfigsCreateBypassMaintenanceWindowErrorComponent
        | ApiV1BlockRolloutConfigsCreateConditionsErrorComponent
        | ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponent
        | ApiV1BlockRolloutConfigsCreateCriticalityErrorComponent
        | ApiV1BlockRolloutConfigsCreateCronExpressionErrorComponent
        | ApiV1BlockRolloutConfigsCreateDebugModeErrorComponent
        | ApiV1BlockRolloutConfigsCreateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutConfigsCreateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponent
        | ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponent
        | ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponent
        | ApiV1BlockRolloutConfigsCreateIsSystemConfigErrorComponent
        | ApiV1BlockRolloutConfigsCreateKindErrorComponent
        | ApiV1BlockRolloutConfigsCreateLabelsErrorComponent
        | ApiV1BlockRolloutConfigsCreateLastStateChangeErrorComponent
        | ApiV1BlockRolloutConfigsCreateLastStateErrorComponent
        | ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponent
        | ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponent
        | ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponent
        | ApiV1BlockRolloutConfigsCreateNameErrorComponent
        | ApiV1BlockRolloutConfigsCreateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutConfigsCreateNotifyOnWaveBlockedErrorComponent
        | ApiV1BlockRolloutConfigsCreatePlatformServiceErrorComponent
        | ApiV1BlockRolloutConfigsCreateProviderErrorComponent
        | ApiV1BlockRolloutConfigsCreateProviderIdErrorComponent
        | ApiV1BlockRolloutConfigsCreateProviderReferenceErrorComponent
        | ApiV1BlockRolloutConfigsCreateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutConfigsCreateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutConfigsCreateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsCreateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsCreateRepairRunningErrorComponent
        | ApiV1BlockRolloutConfigsCreateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsCreateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsCreateScopeErrorComponent
        | ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponent
        | ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponent
        | ApiV1BlockRolloutConfigsCreateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsCreateSloTargetErrorComponent
        | ApiV1BlockRolloutConfigsCreateStateErrorComponent
        | ApiV1BlockRolloutConfigsCreateStateReasonErrorComponent
        | ApiV1BlockRolloutConfigsCreateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponent
        | ApiV1BlockRolloutConfigsCreateTargetVersionErrorComponent
        | ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponent
        | ApiV1BlockRolloutConfigsCreateTemplateBlockErrorComponent
        | ApiV1BlockRolloutConfigsCreateTolerationsErrorComponent
        | ApiV1BlockRolloutConfigsCreateTriggerTypeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollout_configs_create_action_name_error_component import (
            ApiV1BlockRolloutConfigsCreateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_active_error_component import (
            ApiV1BlockRolloutConfigsCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_actual_availability_error_component import (
            ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_annotations_error_component import (
            ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_archived_at_error_component import (
            ApiV1BlockRolloutConfigsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_archived_error_component import (
            ApiV1BlockRolloutConfigsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_archived_reason_error_component import (
            ApiV1BlockRolloutConfigsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_auto_takeover_error_component import (
            ApiV1BlockRolloutConfigsCreateAutoTakeoverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_block_config_template_error_component import (
            ApiV1BlockRolloutConfigsCreateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_block_name_error_component import (
            ApiV1BlockRolloutConfigsCreateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_bypass_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsCreateBypassMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_conditions_error_component import (
            ApiV1BlockRolloutConfigsCreateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_config_to_credential_mappings_error_component import (
            ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_criticality_error_component import (
            ApiV1BlockRolloutConfigsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_cron_expression_error_component import (
            ApiV1BlockRolloutConfigsCreateCronExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_debug_mode_error_component import (
            ApiV1BlockRolloutConfigsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutConfigsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_discovery_running_error_component import (
            ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutConfigsCreateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_display_name_error_component import (
            ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_enqueue_reason_error_component import (
            ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_failure_threshold_percent_error_component import (
            ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_is_system_config_error_component import (
            ApiV1BlockRolloutConfigsCreateIsSystemConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_kind_error_component import (
            ApiV1BlockRolloutConfigsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_labels_error_component import (
            ApiV1BlockRolloutConfigsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_last_state_change_error_component import (
            ApiV1BlockRolloutConfigsCreateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_last_state_error_component import (
            ApiV1BlockRolloutConfigsCreateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_max_concurrent_percent_error_component import (
            ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_max_retries_error_component import (
            ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_name_error_component import (
            ApiV1BlockRolloutConfigsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_non_field_errors_error_component import (
            ApiV1BlockRolloutConfigsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_platform_service_error_component import (
            ApiV1BlockRolloutConfigsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_provider_error_component import (
            ApiV1BlockRolloutConfigsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_provider_id_error_component import (
            ApiV1BlockRolloutConfigsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_provider_reference_error_component import (
            ApiV1BlockRolloutConfigsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutConfigsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutConfigsCreateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutConfigsCreateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutConfigsCreateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_repair_running_error_component import (
            ApiV1BlockRolloutConfigsCreateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_repair_task_id_error_component import (
            ApiV1BlockRolloutConfigsCreateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutConfigsCreateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_scope_error_component import (
            ApiV1BlockRolloutConfigsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_scope_expressions_error_component import (
            ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_sla_availability_error_component import (
            ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_sla_target_error_component import (
            ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_slo_availability_error_component import (
            ApiV1BlockRolloutConfigsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_slo_target_error_component import (
            ApiV1BlockRolloutConfigsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_state_error_component import (
            ApiV1BlockRolloutConfigsCreateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_state_reason_error_component import (
            ApiV1BlockRolloutConfigsCreateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_target_availability_error_component import (
            ApiV1BlockRolloutConfigsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_target_organizations_error_component import (
            ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_target_version_error_component import (
            ApiV1BlockRolloutConfigsCreateTargetVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_target_workspaces_error_component import (
            ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_template_block_error_component import (
            ApiV1BlockRolloutConfigsCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_tolerations_error_component import (
            ApiV1BlockRolloutConfigsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_trigger_type_error_component import (
            ApiV1BlockRolloutConfigsCreateTriggerTypeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateIsSystemConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateTriggerTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateCronExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateActionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateTargetVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateBlockConfigTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateAutoTakeoverErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsCreateBypassMaintenanceWindowErrorComponent):
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
        from ..models.api_v1_block_rollout_configs_create_action_name_error_component import (
            ApiV1BlockRolloutConfigsCreateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_active_error_component import (
            ApiV1BlockRolloutConfigsCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_actual_availability_error_component import (
            ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_annotations_error_component import (
            ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_archived_at_error_component import (
            ApiV1BlockRolloutConfigsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_archived_error_component import (
            ApiV1BlockRolloutConfigsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_archived_reason_error_component import (
            ApiV1BlockRolloutConfigsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_auto_takeover_error_component import (
            ApiV1BlockRolloutConfigsCreateAutoTakeoverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_block_config_template_error_component import (
            ApiV1BlockRolloutConfigsCreateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_block_name_error_component import (
            ApiV1BlockRolloutConfigsCreateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_bypass_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsCreateBypassMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_conditions_error_component import (
            ApiV1BlockRolloutConfigsCreateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_config_to_credential_mappings_error_component import (
            ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_criticality_error_component import (
            ApiV1BlockRolloutConfigsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_cron_expression_error_component import (
            ApiV1BlockRolloutConfigsCreateCronExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_debug_mode_error_component import (
            ApiV1BlockRolloutConfigsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutConfigsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_discovery_running_error_component import (
            ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutConfigsCreateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_display_name_error_component import (
            ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_enqueue_reason_error_component import (
            ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_failure_threshold_percent_error_component import (
            ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_is_system_config_error_component import (
            ApiV1BlockRolloutConfigsCreateIsSystemConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_kind_error_component import (
            ApiV1BlockRolloutConfigsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_labels_error_component import (
            ApiV1BlockRolloutConfigsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_last_state_change_error_component import (
            ApiV1BlockRolloutConfigsCreateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_last_state_error_component import (
            ApiV1BlockRolloutConfigsCreateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_max_concurrent_percent_error_component import (
            ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_max_retries_error_component import (
            ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_name_error_component import (
            ApiV1BlockRolloutConfigsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_non_field_errors_error_component import (
            ApiV1BlockRolloutConfigsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_notify_on_wave_blocked_error_component import (
            ApiV1BlockRolloutConfigsCreateNotifyOnWaveBlockedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_platform_service_error_component import (
            ApiV1BlockRolloutConfigsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_provider_error_component import (
            ApiV1BlockRolloutConfigsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_provider_id_error_component import (
            ApiV1BlockRolloutConfigsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_provider_reference_error_component import (
            ApiV1BlockRolloutConfigsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutConfigsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutConfigsCreateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutConfigsCreateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutConfigsCreateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_repair_running_error_component import (
            ApiV1BlockRolloutConfigsCreateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_repair_task_id_error_component import (
            ApiV1BlockRolloutConfigsCreateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutConfigsCreateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_scope_error_component import (
            ApiV1BlockRolloutConfigsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_scope_expressions_error_component import (
            ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_sla_availability_error_component import (
            ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_sla_target_error_component import (
            ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_slo_availability_error_component import (
            ApiV1BlockRolloutConfigsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_slo_target_error_component import (
            ApiV1BlockRolloutConfigsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_state_error_component import (
            ApiV1BlockRolloutConfigsCreateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_state_reason_error_component import (
            ApiV1BlockRolloutConfigsCreateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_target_availability_error_component import (
            ApiV1BlockRolloutConfigsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_target_organizations_error_component import (
            ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_target_version_error_component import (
            ApiV1BlockRolloutConfigsCreateTargetVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_target_workspaces_error_component import (
            ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_template_block_error_component import (
            ApiV1BlockRolloutConfigsCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_tolerations_error_component import (
            ApiV1BlockRolloutConfigsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_create_trigger_type_error_component import (
            ApiV1BlockRolloutConfigsCreateTriggerTypeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutConfigsCreateActionNameErrorComponent
                | ApiV1BlockRolloutConfigsCreateActiveErrorComponent
                | ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponent
                | ApiV1BlockRolloutConfigsCreateArchivedAtErrorComponent
                | ApiV1BlockRolloutConfigsCreateArchivedErrorComponent
                | ApiV1BlockRolloutConfigsCreateArchivedReasonErrorComponent
                | ApiV1BlockRolloutConfigsCreateAutoTakeoverErrorComponent
                | ApiV1BlockRolloutConfigsCreateBlockConfigTemplateErrorComponent
                | ApiV1BlockRolloutConfigsCreateBlockNameErrorComponent
                | ApiV1BlockRolloutConfigsCreateBypassMaintenanceWindowErrorComponent
                | ApiV1BlockRolloutConfigsCreateConditionsErrorComponent
                | ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponent
                | ApiV1BlockRolloutConfigsCreateCriticalityErrorComponent
                | ApiV1BlockRolloutConfigsCreateCronExpressionErrorComponent
                | ApiV1BlockRolloutConfigsCreateDebugModeErrorComponent
                | ApiV1BlockRolloutConfigsCreateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutConfigsCreateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponent
                | ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponent
                | ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponent
                | ApiV1BlockRolloutConfigsCreateIsSystemConfigErrorComponent
                | ApiV1BlockRolloutConfigsCreateKindErrorComponent
                | ApiV1BlockRolloutConfigsCreateLabelsErrorComponent
                | ApiV1BlockRolloutConfigsCreateLastStateChangeErrorComponent
                | ApiV1BlockRolloutConfigsCreateLastStateErrorComponent
                | ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponent
                | ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponent
                | ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponent
                | ApiV1BlockRolloutConfigsCreateNameErrorComponent
                | ApiV1BlockRolloutConfigsCreateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutConfigsCreateNotifyOnWaveBlockedErrorComponent
                | ApiV1BlockRolloutConfigsCreatePlatformServiceErrorComponent
                | ApiV1BlockRolloutConfigsCreateProviderErrorComponent
                | ApiV1BlockRolloutConfigsCreateProviderIdErrorComponent
                | ApiV1BlockRolloutConfigsCreateProviderReferenceErrorComponent
                | ApiV1BlockRolloutConfigsCreateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutConfigsCreateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutConfigsCreateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsCreateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsCreateRepairRunningErrorComponent
                | ApiV1BlockRolloutConfigsCreateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsCreateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsCreateScopeErrorComponent
                | ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponent
                | ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponent
                | ApiV1BlockRolloutConfigsCreateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsCreateSloTargetErrorComponent
                | ApiV1BlockRolloutConfigsCreateStateErrorComponent
                | ApiV1BlockRolloutConfigsCreateStateReasonErrorComponent
                | ApiV1BlockRolloutConfigsCreateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponent
                | ApiV1BlockRolloutConfigsCreateTargetVersionErrorComponent
                | ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponent
                | ApiV1BlockRolloutConfigsCreateTemplateBlockErrorComponent
                | ApiV1BlockRolloutConfigsCreateTolerationsErrorComponent
                | ApiV1BlockRolloutConfigsCreateTriggerTypeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_0 = (
                        ApiV1BlockRolloutConfigsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_1 = (
                        ApiV1BlockRolloutConfigsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_2 = (
                        ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_3 = (
                        ApiV1BlockRolloutConfigsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_4 = (
                        ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_5 = (
                        ApiV1BlockRolloutConfigsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_6 = (
                        ApiV1BlockRolloutConfigsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_7 = (
                        ApiV1BlockRolloutConfigsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_8 = (
                        ApiV1BlockRolloutConfigsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_9 = (
                        ApiV1BlockRolloutConfigsCreateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_10 = (
                        ApiV1BlockRolloutConfigsCreateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_11 = (
                        ApiV1BlockRolloutConfigsCreateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_12 = (
                        ApiV1BlockRolloutConfigsCreateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_13 = (
                        ApiV1BlockRolloutConfigsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_14 = (
                        ApiV1BlockRolloutConfigsCreateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_15 = (
                        ApiV1BlockRolloutConfigsCreateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_16 = (
                        ApiV1BlockRolloutConfigsCreateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_17 = (
                        ApiV1BlockRolloutConfigsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_18 = (
                        ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_19 = (
                        ApiV1BlockRolloutConfigsCreateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_20 = (
                        ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_21 = (
                        ApiV1BlockRolloutConfigsCreateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_22 = (
                        ApiV1BlockRolloutConfigsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_23 = (
                        ApiV1BlockRolloutConfigsCreateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_24 = (
                        ApiV1BlockRolloutConfigsCreateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_25 = (
                        ApiV1BlockRolloutConfigsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_26 = (
                        ApiV1BlockRolloutConfigsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_27 = (
                        ApiV1BlockRolloutConfigsCreateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_28 = (
                        ApiV1BlockRolloutConfigsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_29 = (
                        ApiV1BlockRolloutConfigsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_30 = (
                        ApiV1BlockRolloutConfigsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_31 = (
                        ApiV1BlockRolloutConfigsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_32 = (
                        ApiV1BlockRolloutConfigsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_33 = (
                        ApiV1BlockRolloutConfigsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_34 = (
                        ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_35 = (
                        ApiV1BlockRolloutConfigsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_36 = (
                        ApiV1BlockRolloutConfigsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_37 = (
                        ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_38 = (
                        ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_39 = (
                        ApiV1BlockRolloutConfigsCreateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_40 = (
                        ApiV1BlockRolloutConfigsCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_41 = (
                        ApiV1BlockRolloutConfigsCreateIsSystemConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_42 = (
                        ApiV1BlockRolloutConfigsCreateTriggerTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_43 = (
                        ApiV1BlockRolloutConfigsCreateCronExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_44 = (
                        ApiV1BlockRolloutConfigsCreateActionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_45 = (
                        ApiV1BlockRolloutConfigsCreateTargetVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_46 = (
                        ApiV1BlockRolloutConfigsCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_47 = (
                        ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_48 = (
                        ApiV1BlockRolloutConfigsCreateBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_49 = (
                        ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_50 = (
                        ApiV1BlockRolloutConfigsCreateAutoTakeoverErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_51 = (
                        ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_52 = (
                        ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_53 = (
                        ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_54 = (
                        ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_55 = (
                        ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_56 = (
                        ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_57 = (
                        ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_create_error_type_58 = (
                        ApiV1BlockRolloutConfigsCreateBypassMaintenanceWindowErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollout_configs_create_error_type_59 = (
                    ApiV1BlockRolloutConfigsCreateNotifyOnWaveBlockedErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollout_configs_create_error_type_59

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollout_configs_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollout_configs_create_validation_error.additional_properties = d
        return api_v1_block_rollout_configs_create_validation_error

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
