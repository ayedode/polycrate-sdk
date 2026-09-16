from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_repair_create_actual_availability_error_component import (
        ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_alternative_name_error_component import (
        ApiV1WorkspacesRepairCreateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_annotations_error_component import (
        ApiV1WorkspacesRepairCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_archived_at_error_component import (
        ApiV1WorkspacesRepairCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_archived_error_component import (
        ApiV1WorkspacesRepairCreateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_archived_reason_error_component import (
        ApiV1WorkspacesRepairCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_backup_enabled_error_component import (
        ApiV1WorkspacesRepairCreateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_criticality_error_component import (
        ApiV1WorkspacesRepairCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_debug_mode_error_component import (
        ApiV1WorkspacesRepairCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_description_error_component import (
        ApiV1WorkspacesRepairCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_discovery_enabled_error_component import (
        ApiV1WorkspacesRepairCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_display_name_error_component import (
        ApiV1WorkspacesRepairCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_encrypted_error_component import (
        ApiV1WorkspacesRepairCreateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesRepairCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_endpoint_monitors_error_component import (
        ApiV1WorkspacesRepairCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_gitlab_project_id_error_component import (
        ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_gitlab_project_url_error_component import (
        ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesRepairCreateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesRepairCreateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_k8s_addons_enabled_error_component import (
        ApiV1WorkspacesRepairCreateK8SAddonsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_kind_error_component import (
        ApiV1WorkspacesRepairCreateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_labels_error_component import (
        ApiV1WorkspacesRepairCreateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_logs_enabled_error_component import (
        ApiV1WorkspacesRepairCreateLogsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_metrics_enabled_error_component import (
        ApiV1WorkspacesRepairCreateMetricsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesRepairCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_name_error_component import (
        ApiV1WorkspacesRepairCreateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_non_field_errors_error_component import (
        ApiV1WorkspacesRepairCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_notifications_enabled_error_component import (
        ApiV1WorkspacesRepairCreateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_on_premise_error_component import (
        ApiV1WorkspacesRepairCreateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_organization_id_error_component import (
        ApiV1WorkspacesRepairCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_owner_id_error_component import (
        ApiV1WorkspacesRepairCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_platform_service_error_component import (
        ApiV1WorkspacesRepairCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_pop_id_error_component import (
        ApiV1WorkspacesRepairCreatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_provider_error_component import (
        ApiV1WorkspacesRepairCreateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_provider_id_error_component import (
        ApiV1WorkspacesRepairCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_provider_reference_error_component import (
        ApiV1WorkspacesRepairCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_purpose_error_component import (
        ApiV1WorkspacesRepairCreatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_readme_md_error_component import (
        ApiV1WorkspacesRepairCreateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_reconciliation_enabled_error_component import (
        ApiV1WorkspacesRepairCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_scope_error_component import (
        ApiV1WorkspacesRepairCreateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_secrets_poly_raw_error_component import (
        ApiV1WorkspacesRepairCreateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_sla_availability_error_component import (
        ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_sla_target_error_component import (
        ApiV1WorkspacesRepairCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_slo_availability_error_component import (
        ApiV1WorkspacesRepairCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_slo_target_error_component import (
        ApiV1WorkspacesRepairCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_target_availability_error_component import (
        ApiV1WorkspacesRepairCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_template_error_component import (
        ApiV1WorkspacesRepairCreateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_urls_error_component import (
        ApiV1WorkspacesRepairCreateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_repair_create_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesRepairCreateValidationError")


@_attrs_define
class ApiV1WorkspacesRepairCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponent |
            ApiV1WorkspacesRepairCreateAlternativeNameErrorComponent | ApiV1WorkspacesRepairCreateAnnotationsErrorComponent
            | ApiV1WorkspacesRepairCreateArchivedAtErrorComponent | ApiV1WorkspacesRepairCreateArchivedErrorComponent |
            ApiV1WorkspacesRepairCreateArchivedReasonErrorComponent | ApiV1WorkspacesRepairCreateBackupEnabledErrorComponent
            | ApiV1WorkspacesRepairCreateCriticalityErrorComponent | ApiV1WorkspacesRepairCreateDebugModeErrorComponent |
            ApiV1WorkspacesRepairCreateDescriptionErrorComponent | ApiV1WorkspacesRepairCreateDiscoveryEnabledErrorComponent
            | ApiV1WorkspacesRepairCreateDisplayNameErrorComponent | ApiV1WorkspacesRepairCreateEncryptedErrorComponent |
            ApiV1WorkspacesRepairCreateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesRepairCreateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesRepairCreateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesRepairCreateHasIncompatibleKubeconfigErrorComponent |
            ApiV1WorkspacesRepairCreateK8SAddonsEnabledErrorComponent | ApiV1WorkspacesRepairCreateKindErrorComponent |
            ApiV1WorkspacesRepairCreateLabelsErrorComponent | ApiV1WorkspacesRepairCreateLogsEnabledErrorComponent |
            ApiV1WorkspacesRepairCreateMetricsEnabledErrorComponent |
            ApiV1WorkspacesRepairCreateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesRepairCreateNameErrorComponent | ApiV1WorkspacesRepairCreateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesRepairCreateNotificationsEnabledErrorComponent |
            ApiV1WorkspacesRepairCreateOnPremiseErrorComponent | ApiV1WorkspacesRepairCreateOrganizationIdErrorComponent |
            ApiV1WorkspacesRepairCreateOwnerIdErrorComponent | ApiV1WorkspacesRepairCreatePlatformServiceErrorComponent |
            ApiV1WorkspacesRepairCreatePopIdErrorComponent | ApiV1WorkspacesRepairCreateProviderErrorComponent |
            ApiV1WorkspacesRepairCreateProviderIdErrorComponent | ApiV1WorkspacesRepairCreateProviderReferenceErrorComponent
            | ApiV1WorkspacesRepairCreatePurposeErrorComponent | ApiV1WorkspacesRepairCreateReadmeMdErrorComponent |
            ApiV1WorkspacesRepairCreateReconciliationEnabledErrorComponent | ApiV1WorkspacesRepairCreateScopeErrorComponent
            | ApiV1WorkspacesRepairCreateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponent | ApiV1WorkspacesRepairCreateSlaTargetErrorComponent |
            ApiV1WorkspacesRepairCreateSloAvailabilityErrorComponent | ApiV1WorkspacesRepairCreateSloTargetErrorComponent |
            ApiV1WorkspacesRepairCreateTargetAvailabilityErrorComponent | ApiV1WorkspacesRepairCreateTemplateErrorComponent
            | ApiV1WorkspacesRepairCreateUrlsErrorComponent |
            ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponent
        | ApiV1WorkspacesRepairCreateAlternativeNameErrorComponent
        | ApiV1WorkspacesRepairCreateAnnotationsErrorComponent
        | ApiV1WorkspacesRepairCreateArchivedAtErrorComponent
        | ApiV1WorkspacesRepairCreateArchivedErrorComponent
        | ApiV1WorkspacesRepairCreateArchivedReasonErrorComponent
        | ApiV1WorkspacesRepairCreateBackupEnabledErrorComponent
        | ApiV1WorkspacesRepairCreateCriticalityErrorComponent
        | ApiV1WorkspacesRepairCreateDebugModeErrorComponent
        | ApiV1WorkspacesRepairCreateDescriptionErrorComponent
        | ApiV1WorkspacesRepairCreateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesRepairCreateDisplayNameErrorComponent
        | ApiV1WorkspacesRepairCreateEncryptedErrorComponent
        | ApiV1WorkspacesRepairCreateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesRepairCreateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesRepairCreateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesRepairCreateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesRepairCreateK8SAddonsEnabledErrorComponent
        | ApiV1WorkspacesRepairCreateKindErrorComponent
        | ApiV1WorkspacesRepairCreateLabelsErrorComponent
        | ApiV1WorkspacesRepairCreateLogsEnabledErrorComponent
        | ApiV1WorkspacesRepairCreateMetricsEnabledErrorComponent
        | ApiV1WorkspacesRepairCreateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesRepairCreateNameErrorComponent
        | ApiV1WorkspacesRepairCreateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesRepairCreateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesRepairCreateOnPremiseErrorComponent
        | ApiV1WorkspacesRepairCreateOrganizationIdErrorComponent
        | ApiV1WorkspacesRepairCreateOwnerIdErrorComponent
        | ApiV1WorkspacesRepairCreatePlatformServiceErrorComponent
        | ApiV1WorkspacesRepairCreatePopIdErrorComponent
        | ApiV1WorkspacesRepairCreateProviderErrorComponent
        | ApiV1WorkspacesRepairCreateProviderIdErrorComponent
        | ApiV1WorkspacesRepairCreateProviderReferenceErrorComponent
        | ApiV1WorkspacesRepairCreatePurposeErrorComponent
        | ApiV1WorkspacesRepairCreateReadmeMdErrorComponent
        | ApiV1WorkspacesRepairCreateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesRepairCreateScopeErrorComponent
        | ApiV1WorkspacesRepairCreateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesRepairCreateSlaTargetErrorComponent
        | ApiV1WorkspacesRepairCreateSloAvailabilityErrorComponent
        | ApiV1WorkspacesRepairCreateSloTargetErrorComponent
        | ApiV1WorkspacesRepairCreateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesRepairCreateTemplateErrorComponent
        | ApiV1WorkspacesRepairCreateUrlsErrorComponent
        | ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_repair_create_actual_availability_error_component import (
            ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_annotations_error_component import (
            ApiV1WorkspacesRepairCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_archived_at_error_component import (
            ApiV1WorkspacesRepairCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_archived_error_component import (
            ApiV1WorkspacesRepairCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_archived_reason_error_component import (
            ApiV1WorkspacesRepairCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_backup_enabled_error_component import (
            ApiV1WorkspacesRepairCreateBackupEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_criticality_error_component import (
            ApiV1WorkspacesRepairCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_debug_mode_error_component import (
            ApiV1WorkspacesRepairCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_description_error_component import (
            ApiV1WorkspacesRepairCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_discovery_enabled_error_component import (
            ApiV1WorkspacesRepairCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_display_name_error_component import (
            ApiV1WorkspacesRepairCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_encrypted_error_component import (
            ApiV1WorkspacesRepairCreateEncryptedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesRepairCreateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesRepairCreateEndpointMonitorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesRepairCreateGlobalEndpointMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesRepairCreateHasIncompatibleKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_k8s_addons_enabled_error_component import (
            ApiV1WorkspacesRepairCreateK8SAddonsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_kind_error_component import (
            ApiV1WorkspacesRepairCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_labels_error_component import (
            ApiV1WorkspacesRepairCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_logs_enabled_error_component import (
            ApiV1WorkspacesRepairCreateLogsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_metrics_enabled_error_component import (
            ApiV1WorkspacesRepairCreateMetricsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesRepairCreateMonitoringWorkspaceAllowlistIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_name_error_component import (
            ApiV1WorkspacesRepairCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_non_field_errors_error_component import (
            ApiV1WorkspacesRepairCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_notifications_enabled_error_component import (
            ApiV1WorkspacesRepairCreateNotificationsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_on_premise_error_component import (
            ApiV1WorkspacesRepairCreateOnPremiseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_organization_id_error_component import (
            ApiV1WorkspacesRepairCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_owner_id_error_component import (
            ApiV1WorkspacesRepairCreateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_platform_service_error_component import (
            ApiV1WorkspacesRepairCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_pop_id_error_component import (
            ApiV1WorkspacesRepairCreatePopIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_provider_error_component import (
            ApiV1WorkspacesRepairCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_provider_id_error_component import (
            ApiV1WorkspacesRepairCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_provider_reference_error_component import (
            ApiV1WorkspacesRepairCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_purpose_error_component import (
            ApiV1WorkspacesRepairCreatePurposeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_readme_md_error_component import (
            ApiV1WorkspacesRepairCreateReadmeMdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesRepairCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_scope_error_component import (
            ApiV1WorkspacesRepairCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesRepairCreateSecretsPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_sla_availability_error_component import (
            ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_sla_target_error_component import (
            ApiV1WorkspacesRepairCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_slo_availability_error_component import (
            ApiV1WorkspacesRepairCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_slo_target_error_component import (
            ApiV1WorkspacesRepairCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_target_availability_error_component import (
            ApiV1WorkspacesRepairCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_template_error_component import (
            ApiV1WorkspacesRepairCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_urls_error_component import (
            ApiV1WorkspacesRepairCreateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesRepairCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateMonitoringWorkspaceAllowlistIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateMetricsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateLogsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateK8SAddonsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesRepairCreateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_repair_create_actual_availability_error_component import (
            ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_alternative_name_error_component import (
            ApiV1WorkspacesRepairCreateAlternativeNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_annotations_error_component import (
            ApiV1WorkspacesRepairCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_archived_at_error_component import (
            ApiV1WorkspacesRepairCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_archived_error_component import (
            ApiV1WorkspacesRepairCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_archived_reason_error_component import (
            ApiV1WorkspacesRepairCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_backup_enabled_error_component import (
            ApiV1WorkspacesRepairCreateBackupEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_criticality_error_component import (
            ApiV1WorkspacesRepairCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_debug_mode_error_component import (
            ApiV1WorkspacesRepairCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_description_error_component import (
            ApiV1WorkspacesRepairCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_discovery_enabled_error_component import (
            ApiV1WorkspacesRepairCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_display_name_error_component import (
            ApiV1WorkspacesRepairCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_encrypted_error_component import (
            ApiV1WorkspacesRepairCreateEncryptedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesRepairCreateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesRepairCreateEndpointMonitorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesRepairCreateGlobalEndpointMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesRepairCreateHasIncompatibleKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_k8s_addons_enabled_error_component import (
            ApiV1WorkspacesRepairCreateK8SAddonsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_kind_error_component import (
            ApiV1WorkspacesRepairCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_labels_error_component import (
            ApiV1WorkspacesRepairCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_logs_enabled_error_component import (
            ApiV1WorkspacesRepairCreateLogsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_metrics_enabled_error_component import (
            ApiV1WorkspacesRepairCreateMetricsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesRepairCreateMonitoringWorkspaceAllowlistIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_name_error_component import (
            ApiV1WorkspacesRepairCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_non_field_errors_error_component import (
            ApiV1WorkspacesRepairCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_notifications_enabled_error_component import (
            ApiV1WorkspacesRepairCreateNotificationsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_on_premise_error_component import (
            ApiV1WorkspacesRepairCreateOnPremiseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_organization_id_error_component import (
            ApiV1WorkspacesRepairCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_owner_id_error_component import (
            ApiV1WorkspacesRepairCreateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_platform_service_error_component import (
            ApiV1WorkspacesRepairCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_pop_id_error_component import (
            ApiV1WorkspacesRepairCreatePopIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_provider_error_component import (
            ApiV1WorkspacesRepairCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_provider_id_error_component import (
            ApiV1WorkspacesRepairCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_provider_reference_error_component import (
            ApiV1WorkspacesRepairCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_purpose_error_component import (
            ApiV1WorkspacesRepairCreatePurposeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_readme_md_error_component import (
            ApiV1WorkspacesRepairCreateReadmeMdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesRepairCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_scope_error_component import (
            ApiV1WorkspacesRepairCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesRepairCreateSecretsPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_sla_availability_error_component import (
            ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_sla_target_error_component import (
            ApiV1WorkspacesRepairCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_slo_availability_error_component import (
            ApiV1WorkspacesRepairCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_slo_target_error_component import (
            ApiV1WorkspacesRepairCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_target_availability_error_component import (
            ApiV1WorkspacesRepairCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_template_error_component import (
            ApiV1WorkspacesRepairCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_urls_error_component import (
            ApiV1WorkspacesRepairCreateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_repair_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponent
                | ApiV1WorkspacesRepairCreateAlternativeNameErrorComponent
                | ApiV1WorkspacesRepairCreateAnnotationsErrorComponent
                | ApiV1WorkspacesRepairCreateArchivedAtErrorComponent
                | ApiV1WorkspacesRepairCreateArchivedErrorComponent
                | ApiV1WorkspacesRepairCreateArchivedReasonErrorComponent
                | ApiV1WorkspacesRepairCreateBackupEnabledErrorComponent
                | ApiV1WorkspacesRepairCreateCriticalityErrorComponent
                | ApiV1WorkspacesRepairCreateDebugModeErrorComponent
                | ApiV1WorkspacesRepairCreateDescriptionErrorComponent
                | ApiV1WorkspacesRepairCreateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesRepairCreateDisplayNameErrorComponent
                | ApiV1WorkspacesRepairCreateEncryptedErrorComponent
                | ApiV1WorkspacesRepairCreateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesRepairCreateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesRepairCreateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesRepairCreateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesRepairCreateK8SAddonsEnabledErrorComponent
                | ApiV1WorkspacesRepairCreateKindErrorComponent
                | ApiV1WorkspacesRepairCreateLabelsErrorComponent
                | ApiV1WorkspacesRepairCreateLogsEnabledErrorComponent
                | ApiV1WorkspacesRepairCreateMetricsEnabledErrorComponent
                | ApiV1WorkspacesRepairCreateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesRepairCreateNameErrorComponent
                | ApiV1WorkspacesRepairCreateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesRepairCreateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesRepairCreateOnPremiseErrorComponent
                | ApiV1WorkspacesRepairCreateOrganizationIdErrorComponent
                | ApiV1WorkspacesRepairCreateOwnerIdErrorComponent
                | ApiV1WorkspacesRepairCreatePlatformServiceErrorComponent
                | ApiV1WorkspacesRepairCreatePopIdErrorComponent
                | ApiV1WorkspacesRepairCreateProviderErrorComponent
                | ApiV1WorkspacesRepairCreateProviderIdErrorComponent
                | ApiV1WorkspacesRepairCreateProviderReferenceErrorComponent
                | ApiV1WorkspacesRepairCreatePurposeErrorComponent
                | ApiV1WorkspacesRepairCreateReadmeMdErrorComponent
                | ApiV1WorkspacesRepairCreateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesRepairCreateScopeErrorComponent
                | ApiV1WorkspacesRepairCreateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesRepairCreateSlaTargetErrorComponent
                | ApiV1WorkspacesRepairCreateSloAvailabilityErrorComponent
                | ApiV1WorkspacesRepairCreateSloTargetErrorComponent
                | ApiV1WorkspacesRepairCreateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesRepairCreateTemplateErrorComponent
                | ApiV1WorkspacesRepairCreateUrlsErrorComponent
                | ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_0 = (
                        ApiV1WorkspacesRepairCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_1 = (
                        ApiV1WorkspacesRepairCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_2 = (
                        ApiV1WorkspacesRepairCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_3 = (
                        ApiV1WorkspacesRepairCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_4 = (
                        ApiV1WorkspacesRepairCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_5 = (
                        ApiV1WorkspacesRepairCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_6 = (
                        ApiV1WorkspacesRepairCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_7 = (
                        ApiV1WorkspacesRepairCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_8 = (
                        ApiV1WorkspacesRepairCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_9 = (
                        ApiV1WorkspacesRepairCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_10 = (
                        ApiV1WorkspacesRepairCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_11 = (
                        ApiV1WorkspacesRepairCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_12 = (
                        ApiV1WorkspacesRepairCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_13 = (
                        ApiV1WorkspacesRepairCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_14 = (
                        ApiV1WorkspacesRepairCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_15 = (
                        ApiV1WorkspacesRepairCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_16 = (
                        ApiV1WorkspacesRepairCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_17 = (
                        ApiV1WorkspacesRepairCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_18 = (
                        ApiV1WorkspacesRepairCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_19 = (
                        ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_20 = (
                        ApiV1WorkspacesRepairCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_21 = (
                        ApiV1WorkspacesRepairCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_22 = (
                        ApiV1WorkspacesRepairCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_23 = (
                        ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_24 = (
                        ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_25 = (
                        ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_26 = (
                        ApiV1WorkspacesRepairCreateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_27 = (
                        ApiV1WorkspacesRepairCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_28 = (
                        ApiV1WorkspacesRepairCreateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_29 = (
                        ApiV1WorkspacesRepairCreateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_30 = (
                        ApiV1WorkspacesRepairCreateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_31 = (
                        ApiV1WorkspacesRepairCreateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_32 = (
                        ApiV1WorkspacesRepairCreateMetricsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_33 = (
                        ApiV1WorkspacesRepairCreateLogsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_34 = (
                        ApiV1WorkspacesRepairCreateK8SAddonsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_35 = (
                        ApiV1WorkspacesRepairCreateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_36 = (
                        ApiV1WorkspacesRepairCreateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_37 = (
                        ApiV1WorkspacesRepairCreateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_38 = (
                        ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_39 = (
                        ApiV1WorkspacesRepairCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_40 = (
                        ApiV1WorkspacesRepairCreateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_41 = (
                        ApiV1WorkspacesRepairCreatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_42 = (
                        ApiV1WorkspacesRepairCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_43 = (
                        ApiV1WorkspacesRepairCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_44 = (
                        ApiV1WorkspacesRepairCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_45 = (
                        ApiV1WorkspacesRepairCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_46 = (
                        ApiV1WorkspacesRepairCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_repair_create_error_type_47 = (
                        ApiV1WorkspacesRepairCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_repair_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_repair_create_error_type_48 = (
                    ApiV1WorkspacesRepairCreateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_repair_create_error_type_48

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_repair_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_repair_create_validation_error.additional_properties = d
        return api_v1_workspaces_repair_create_validation_error

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
