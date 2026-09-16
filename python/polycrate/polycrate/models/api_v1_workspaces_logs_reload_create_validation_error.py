from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_logs_reload_create_actual_availability_error_component import (
        ApiV1WorkspacesLogsReloadCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_alternative_name_error_component import (
        ApiV1WorkspacesLogsReloadCreateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_annotations_error_component import (
        ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_archived_at_error_component import (
        ApiV1WorkspacesLogsReloadCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_archived_error_component import (
        ApiV1WorkspacesLogsReloadCreateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_archived_reason_error_component import (
        ApiV1WorkspacesLogsReloadCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_backup_enabled_error_component import (
        ApiV1WorkspacesLogsReloadCreateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_criticality_error_component import (
        ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_debug_mode_error_component import (
        ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_description_error_component import (
        ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_discovery_enabled_error_component import (
        ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_display_name_error_component import (
        ApiV1WorkspacesLogsReloadCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_encrypted_error_component import (
        ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesLogsReloadCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_endpoint_monitors_error_component import (
        ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_gitlab_project_id_error_component import (
        ApiV1WorkspacesLogsReloadCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_gitlab_project_url_error_component import (
        ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesLogsReloadCreateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesLogsReloadCreateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_k8s_addons_enabled_error_component import (
        ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_kind_error_component import (
        ApiV1WorkspacesLogsReloadCreateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_labels_error_component import (
        ApiV1WorkspacesLogsReloadCreateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_logs_enabled_error_component import (
        ApiV1WorkspacesLogsReloadCreateLogsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_metrics_enabled_error_component import (
        ApiV1WorkspacesLogsReloadCreateMetricsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_name_error_component import (
        ApiV1WorkspacesLogsReloadCreateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_non_field_errors_error_component import (
        ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_notifications_enabled_error_component import (
        ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_on_premise_error_component import (
        ApiV1WorkspacesLogsReloadCreateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_organization_id_error_component import (
        ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_owner_id_error_component import (
        ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_platform_service_error_component import (
        ApiV1WorkspacesLogsReloadCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_pop_id_error_component import (
        ApiV1WorkspacesLogsReloadCreatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_provider_error_component import (
        ApiV1WorkspacesLogsReloadCreateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_provider_id_error_component import (
        ApiV1WorkspacesLogsReloadCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_provider_reference_error_component import (
        ApiV1WorkspacesLogsReloadCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_purpose_error_component import (
        ApiV1WorkspacesLogsReloadCreatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_readme_md_error_component import (
        ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_reconciliation_enabled_error_component import (
        ApiV1WorkspacesLogsReloadCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_scope_error_component import (
        ApiV1WorkspacesLogsReloadCreateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_secrets_poly_raw_error_component import (
        ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_sla_availability_error_component import (
        ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_sla_target_error_component import (
        ApiV1WorkspacesLogsReloadCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_slo_availability_error_component import (
        ApiV1WorkspacesLogsReloadCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_slo_target_error_component import (
        ApiV1WorkspacesLogsReloadCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_target_availability_error_component import (
        ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_template_error_component import (
        ApiV1WorkspacesLogsReloadCreateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_urls_error_component import (
        ApiV1WorkspacesLogsReloadCreateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_logs_reload_create_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesLogsReloadCreateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesLogsReloadCreateValidationError")


@_attrs_define
class ApiV1WorkspacesLogsReloadCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesLogsReloadCreateActualAvailabilityErrorComponent |
            ApiV1WorkspacesLogsReloadCreateAlternativeNameErrorComponent |
            ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponent |
            ApiV1WorkspacesLogsReloadCreateArchivedAtErrorComponent | ApiV1WorkspacesLogsReloadCreateArchivedErrorComponent
            | ApiV1WorkspacesLogsReloadCreateArchivedReasonErrorComponent |
            ApiV1WorkspacesLogsReloadCreateBackupEnabledErrorComponent |
            ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponent |
            ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponent |
            ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponent |
            ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesLogsReloadCreateDisplayNameErrorComponent |
            ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponent |
            ApiV1WorkspacesLogsReloadCreateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesLogsReloadCreateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesLogsReloadCreateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesLogsReloadCreateHasIncompatibleKubeconfigErrorComponent |
            ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponent |
            ApiV1WorkspacesLogsReloadCreateKindErrorComponent | ApiV1WorkspacesLogsReloadCreateLabelsErrorComponent |
            ApiV1WorkspacesLogsReloadCreateLogsEnabledErrorComponent |
            ApiV1WorkspacesLogsReloadCreateMetricsEnabledErrorComponent |
            ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesLogsReloadCreateNameErrorComponent | ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponent
            | ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponent |
            ApiV1WorkspacesLogsReloadCreateOnPremiseErrorComponent |
            ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponent |
            ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponent |
            ApiV1WorkspacesLogsReloadCreatePlatformServiceErrorComponent |
            ApiV1WorkspacesLogsReloadCreatePopIdErrorComponent | ApiV1WorkspacesLogsReloadCreateProviderErrorComponent |
            ApiV1WorkspacesLogsReloadCreateProviderIdErrorComponent |
            ApiV1WorkspacesLogsReloadCreateProviderReferenceErrorComponent |
            ApiV1WorkspacesLogsReloadCreatePurposeErrorComponent | ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponent |
            ApiV1WorkspacesLogsReloadCreateReconciliationEnabledErrorComponent |
            ApiV1WorkspacesLogsReloadCreateScopeErrorComponent | ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponent
            | ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponent |
            ApiV1WorkspacesLogsReloadCreateSlaTargetErrorComponent |
            ApiV1WorkspacesLogsReloadCreateSloAvailabilityErrorComponent |
            ApiV1WorkspacesLogsReloadCreateSloTargetErrorComponent |
            ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponent |
            ApiV1WorkspacesLogsReloadCreateTemplateErrorComponent | ApiV1WorkspacesLogsReloadCreateUrlsErrorComponent |
            ApiV1WorkspacesLogsReloadCreateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesLogsReloadCreateActualAvailabilityErrorComponent
        | ApiV1WorkspacesLogsReloadCreateAlternativeNameErrorComponent
        | ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponent
        | ApiV1WorkspacesLogsReloadCreateArchivedAtErrorComponent
        | ApiV1WorkspacesLogsReloadCreateArchivedErrorComponent
        | ApiV1WorkspacesLogsReloadCreateArchivedReasonErrorComponent
        | ApiV1WorkspacesLogsReloadCreateBackupEnabledErrorComponent
        | ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponent
        | ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponent
        | ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponent
        | ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesLogsReloadCreateDisplayNameErrorComponent
        | ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponent
        | ApiV1WorkspacesLogsReloadCreateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesLogsReloadCreateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesLogsReloadCreateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesLogsReloadCreateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponent
        | ApiV1WorkspacesLogsReloadCreateKindErrorComponent
        | ApiV1WorkspacesLogsReloadCreateLabelsErrorComponent
        | ApiV1WorkspacesLogsReloadCreateLogsEnabledErrorComponent
        | ApiV1WorkspacesLogsReloadCreateMetricsEnabledErrorComponent
        | ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesLogsReloadCreateNameErrorComponent
        | ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesLogsReloadCreateOnPremiseErrorComponent
        | ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponent
        | ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponent
        | ApiV1WorkspacesLogsReloadCreatePlatformServiceErrorComponent
        | ApiV1WorkspacesLogsReloadCreatePopIdErrorComponent
        | ApiV1WorkspacesLogsReloadCreateProviderErrorComponent
        | ApiV1WorkspacesLogsReloadCreateProviderIdErrorComponent
        | ApiV1WorkspacesLogsReloadCreateProviderReferenceErrorComponent
        | ApiV1WorkspacesLogsReloadCreatePurposeErrorComponent
        | ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponent
        | ApiV1WorkspacesLogsReloadCreateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesLogsReloadCreateScopeErrorComponent
        | ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesLogsReloadCreateSlaTargetErrorComponent
        | ApiV1WorkspacesLogsReloadCreateSloAvailabilityErrorComponent
        | ApiV1WorkspacesLogsReloadCreateSloTargetErrorComponent
        | ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesLogsReloadCreateTemplateErrorComponent
        | ApiV1WorkspacesLogsReloadCreateUrlsErrorComponent
        | ApiV1WorkspacesLogsReloadCreateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_logs_reload_create_actual_availability_error_component import (
            ApiV1WorkspacesLogsReloadCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_annotations_error_component import (
            ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_archived_at_error_component import (
            ApiV1WorkspacesLogsReloadCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_archived_error_component import (
            ApiV1WorkspacesLogsReloadCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_archived_reason_error_component import (
            ApiV1WorkspacesLogsReloadCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_backup_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateBackupEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_criticality_error_component import (
            ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_debug_mode_error_component import (
            ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_description_error_component import (
            ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_discovery_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_display_name_error_component import (
            ApiV1WorkspacesLogsReloadCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_encrypted_error_component import (
            ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesLogsReloadCreateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesLogsReloadCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesLogsReloadCreateGlobalEndpointMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesLogsReloadCreateHasIncompatibleKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_k8s_addons_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_kind_error_component import (
            ApiV1WorkspacesLogsReloadCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_labels_error_component import (
            ApiV1WorkspacesLogsReloadCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_logs_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateLogsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_metrics_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateMetricsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_name_error_component import (
            ApiV1WorkspacesLogsReloadCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_non_field_errors_error_component import (
            ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_notifications_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_on_premise_error_component import (
            ApiV1WorkspacesLogsReloadCreateOnPremiseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_organization_id_error_component import (
            ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_owner_id_error_component import (
            ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_platform_service_error_component import (
            ApiV1WorkspacesLogsReloadCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_pop_id_error_component import (
            ApiV1WorkspacesLogsReloadCreatePopIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_provider_error_component import (
            ApiV1WorkspacesLogsReloadCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_provider_id_error_component import (
            ApiV1WorkspacesLogsReloadCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_provider_reference_error_component import (
            ApiV1WorkspacesLogsReloadCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_purpose_error_component import (
            ApiV1WorkspacesLogsReloadCreatePurposeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_readme_md_error_component import (
            ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_scope_error_component import (
            ApiV1WorkspacesLogsReloadCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_sla_availability_error_component import (
            ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_sla_target_error_component import (
            ApiV1WorkspacesLogsReloadCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_slo_availability_error_component import (
            ApiV1WorkspacesLogsReloadCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_slo_target_error_component import (
            ApiV1WorkspacesLogsReloadCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_target_availability_error_component import (
            ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_template_error_component import (
            ApiV1WorkspacesLogsReloadCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_urls_error_component import (
            ApiV1WorkspacesLogsReloadCreateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesLogsReloadCreateWorkspaceInventoryRawErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateMetricsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateLogsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_logs_reload_create_actual_availability_error_component import (
            ApiV1WorkspacesLogsReloadCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_alternative_name_error_component import (
            ApiV1WorkspacesLogsReloadCreateAlternativeNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_annotations_error_component import (
            ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_archived_at_error_component import (
            ApiV1WorkspacesLogsReloadCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_archived_error_component import (
            ApiV1WorkspacesLogsReloadCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_archived_reason_error_component import (
            ApiV1WorkspacesLogsReloadCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_backup_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateBackupEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_criticality_error_component import (
            ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_debug_mode_error_component import (
            ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_description_error_component import (
            ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_discovery_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_display_name_error_component import (
            ApiV1WorkspacesLogsReloadCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_encrypted_error_component import (
            ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesLogsReloadCreateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesLogsReloadCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesLogsReloadCreateGlobalEndpointMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesLogsReloadCreateHasIncompatibleKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_k8s_addons_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_kind_error_component import (
            ApiV1WorkspacesLogsReloadCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_labels_error_component import (
            ApiV1WorkspacesLogsReloadCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_logs_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateLogsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_metrics_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateMetricsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_name_error_component import (
            ApiV1WorkspacesLogsReloadCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_non_field_errors_error_component import (
            ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_notifications_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_on_premise_error_component import (
            ApiV1WorkspacesLogsReloadCreateOnPremiseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_organization_id_error_component import (
            ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_owner_id_error_component import (
            ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_platform_service_error_component import (
            ApiV1WorkspacesLogsReloadCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_pop_id_error_component import (
            ApiV1WorkspacesLogsReloadCreatePopIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_provider_error_component import (
            ApiV1WorkspacesLogsReloadCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_provider_id_error_component import (
            ApiV1WorkspacesLogsReloadCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_provider_reference_error_component import (
            ApiV1WorkspacesLogsReloadCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_purpose_error_component import (
            ApiV1WorkspacesLogsReloadCreatePurposeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_readme_md_error_component import (
            ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesLogsReloadCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_scope_error_component import (
            ApiV1WorkspacesLogsReloadCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_sla_availability_error_component import (
            ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_sla_target_error_component import (
            ApiV1WorkspacesLogsReloadCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_slo_availability_error_component import (
            ApiV1WorkspacesLogsReloadCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_slo_target_error_component import (
            ApiV1WorkspacesLogsReloadCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_target_availability_error_component import (
            ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_template_error_component import (
            ApiV1WorkspacesLogsReloadCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_urls_error_component import (
            ApiV1WorkspacesLogsReloadCreateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_logs_reload_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesLogsReloadCreateWorkspaceInventoryRawErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesLogsReloadCreateActualAvailabilityErrorComponent
                | ApiV1WorkspacesLogsReloadCreateAlternativeNameErrorComponent
                | ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponent
                | ApiV1WorkspacesLogsReloadCreateArchivedAtErrorComponent
                | ApiV1WorkspacesLogsReloadCreateArchivedErrorComponent
                | ApiV1WorkspacesLogsReloadCreateArchivedReasonErrorComponent
                | ApiV1WorkspacesLogsReloadCreateBackupEnabledErrorComponent
                | ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponent
                | ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponent
                | ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponent
                | ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesLogsReloadCreateDisplayNameErrorComponent
                | ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponent
                | ApiV1WorkspacesLogsReloadCreateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesLogsReloadCreateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesLogsReloadCreateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesLogsReloadCreateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponent
                | ApiV1WorkspacesLogsReloadCreateKindErrorComponent
                | ApiV1WorkspacesLogsReloadCreateLabelsErrorComponent
                | ApiV1WorkspacesLogsReloadCreateLogsEnabledErrorComponent
                | ApiV1WorkspacesLogsReloadCreateMetricsEnabledErrorComponent
                | ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesLogsReloadCreateNameErrorComponent
                | ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesLogsReloadCreateOnPremiseErrorComponent
                | ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponent
                | ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponent
                | ApiV1WorkspacesLogsReloadCreatePlatformServiceErrorComponent
                | ApiV1WorkspacesLogsReloadCreatePopIdErrorComponent
                | ApiV1WorkspacesLogsReloadCreateProviderErrorComponent
                | ApiV1WorkspacesLogsReloadCreateProviderIdErrorComponent
                | ApiV1WorkspacesLogsReloadCreateProviderReferenceErrorComponent
                | ApiV1WorkspacesLogsReloadCreatePurposeErrorComponent
                | ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponent
                | ApiV1WorkspacesLogsReloadCreateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesLogsReloadCreateScopeErrorComponent
                | ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesLogsReloadCreateSlaTargetErrorComponent
                | ApiV1WorkspacesLogsReloadCreateSloAvailabilityErrorComponent
                | ApiV1WorkspacesLogsReloadCreateSloTargetErrorComponent
                | ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesLogsReloadCreateTemplateErrorComponent
                | ApiV1WorkspacesLogsReloadCreateUrlsErrorComponent
                | ApiV1WorkspacesLogsReloadCreateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_0 = (
                        ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_1 = (
                        ApiV1WorkspacesLogsReloadCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_2 = (
                        ApiV1WorkspacesLogsReloadCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_3 = (
                        ApiV1WorkspacesLogsReloadCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_4 = (
                        ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_5 = (
                        ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_6 = (
                        ApiV1WorkspacesLogsReloadCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_7 = (
                        ApiV1WorkspacesLogsReloadCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_8 = (
                        ApiV1WorkspacesLogsReloadCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_9 = (
                        ApiV1WorkspacesLogsReloadCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_10 = (
                        ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_11 = (
                        ApiV1WorkspacesLogsReloadCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_12 = (
                        ApiV1WorkspacesLogsReloadCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_13 = (
                        ApiV1WorkspacesLogsReloadCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_14 = (
                        ApiV1WorkspacesLogsReloadCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_15 = (
                        ApiV1WorkspacesLogsReloadCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_16 = (
                        ApiV1WorkspacesLogsReloadCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_17 = (
                        ApiV1WorkspacesLogsReloadCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_18 = (
                        ApiV1WorkspacesLogsReloadCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_19 = (
                        ApiV1WorkspacesLogsReloadCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_20 = (
                        ApiV1WorkspacesLogsReloadCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_21 = (
                        ApiV1WorkspacesLogsReloadCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_22 = (
                        ApiV1WorkspacesLogsReloadCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_23 = (
                        ApiV1WorkspacesLogsReloadCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_24 = (
                        ApiV1WorkspacesLogsReloadCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_25 = (
                        ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_26 = (
                        ApiV1WorkspacesLogsReloadCreateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_27 = (
                        ApiV1WorkspacesLogsReloadCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_28 = (
                        ApiV1WorkspacesLogsReloadCreateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_29 = (
                        ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_30 = (
                        ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_31 = (
                        ApiV1WorkspacesLogsReloadCreateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_32 = (
                        ApiV1WorkspacesLogsReloadCreateMetricsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_33 = (
                        ApiV1WorkspacesLogsReloadCreateLogsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_34 = (
                        ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_35 = (
                        ApiV1WorkspacesLogsReloadCreateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_36 = (
                        ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_37 = (
                        ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_38 = (
                        ApiV1WorkspacesLogsReloadCreateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_39 = (
                        ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_40 = (
                        ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_41 = (
                        ApiV1WorkspacesLogsReloadCreatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_42 = (
                        ApiV1WorkspacesLogsReloadCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_43 = (
                        ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_44 = (
                        ApiV1WorkspacesLogsReloadCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_45 = (
                        ApiV1WorkspacesLogsReloadCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_46 = (
                        ApiV1WorkspacesLogsReloadCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_logs_reload_create_error_type_47 = (
                        ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_logs_reload_create_error_type_48 = (
                    ApiV1WorkspacesLogsReloadCreateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_logs_reload_create_error_type_48

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_logs_reload_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_logs_reload_create_validation_error.additional_properties = d
        return api_v1_workspaces_logs_reload_create_validation_error

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
