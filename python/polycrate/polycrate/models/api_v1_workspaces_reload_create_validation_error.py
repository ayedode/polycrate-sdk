from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_reload_create_actual_availability_error_component import (
        ApiV1WorkspacesReloadCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_alternative_name_error_component import (
        ApiV1WorkspacesReloadCreateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_annotations_error_component import (
        ApiV1WorkspacesReloadCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_archived_at_error_component import (
        ApiV1WorkspacesReloadCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_archived_error_component import (
        ApiV1WorkspacesReloadCreateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_archived_reason_error_component import (
        ApiV1WorkspacesReloadCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_backup_enabled_error_component import (
        ApiV1WorkspacesReloadCreateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_criticality_error_component import (
        ApiV1WorkspacesReloadCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_debug_mode_error_component import (
        ApiV1WorkspacesReloadCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_description_error_component import (
        ApiV1WorkspacesReloadCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_discovery_enabled_error_component import (
        ApiV1WorkspacesReloadCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_display_name_error_component import (
        ApiV1WorkspacesReloadCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_encrypted_error_component import (
        ApiV1WorkspacesReloadCreateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesReloadCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_endpoint_monitors_error_component import (
        ApiV1WorkspacesReloadCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_gitlab_project_id_error_component import (
        ApiV1WorkspacesReloadCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_gitlab_project_url_error_component import (
        ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesReloadCreateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesReloadCreateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_k8s_addons_enabled_error_component import (
        ApiV1WorkspacesReloadCreateK8SAddonsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_kind_error_component import (
        ApiV1WorkspacesReloadCreateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_labels_error_component import (
        ApiV1WorkspacesReloadCreateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_logs_enabled_error_component import (
        ApiV1WorkspacesReloadCreateLogsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_metrics_enabled_error_component import (
        ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_name_error_component import (
        ApiV1WorkspacesReloadCreateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_non_field_errors_error_component import (
        ApiV1WorkspacesReloadCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_notifications_enabled_error_component import (
        ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_on_premise_error_component import (
        ApiV1WorkspacesReloadCreateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_organization_id_error_component import (
        ApiV1WorkspacesReloadCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_owner_id_error_component import (
        ApiV1WorkspacesReloadCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_platform_service_error_component import (
        ApiV1WorkspacesReloadCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_pop_id_error_component import (
        ApiV1WorkspacesReloadCreatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_provider_error_component import (
        ApiV1WorkspacesReloadCreateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_provider_id_error_component import (
        ApiV1WorkspacesReloadCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_provider_reference_error_component import (
        ApiV1WorkspacesReloadCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_purpose_error_component import (
        ApiV1WorkspacesReloadCreatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_readme_md_error_component import (
        ApiV1WorkspacesReloadCreateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_reconciliation_enabled_error_component import (
        ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_scope_error_component import (
        ApiV1WorkspacesReloadCreateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_secrets_poly_raw_error_component import (
        ApiV1WorkspacesReloadCreateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_sla_availability_error_component import (
        ApiV1WorkspacesReloadCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_sla_target_error_component import (
        ApiV1WorkspacesReloadCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_slo_availability_error_component import (
        ApiV1WorkspacesReloadCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_slo_target_error_component import (
        ApiV1WorkspacesReloadCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_target_availability_error_component import (
        ApiV1WorkspacesReloadCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_template_error_component import (
        ApiV1WorkspacesReloadCreateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_urls_error_component import (
        ApiV1WorkspacesReloadCreateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_reload_create_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesReloadCreateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesReloadCreateValidationError")


@_attrs_define
class ApiV1WorkspacesReloadCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesReloadCreateActualAvailabilityErrorComponent |
            ApiV1WorkspacesReloadCreateAlternativeNameErrorComponent | ApiV1WorkspacesReloadCreateAnnotationsErrorComponent
            | ApiV1WorkspacesReloadCreateArchivedAtErrorComponent | ApiV1WorkspacesReloadCreateArchivedErrorComponent |
            ApiV1WorkspacesReloadCreateArchivedReasonErrorComponent | ApiV1WorkspacesReloadCreateBackupEnabledErrorComponent
            | ApiV1WorkspacesReloadCreateCriticalityErrorComponent | ApiV1WorkspacesReloadCreateDebugModeErrorComponent |
            ApiV1WorkspacesReloadCreateDescriptionErrorComponent | ApiV1WorkspacesReloadCreateDiscoveryEnabledErrorComponent
            | ApiV1WorkspacesReloadCreateDisplayNameErrorComponent | ApiV1WorkspacesReloadCreateEncryptedErrorComponent |
            ApiV1WorkspacesReloadCreateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesReloadCreateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesReloadCreateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesReloadCreateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesReloadCreateHasIncompatibleKubeconfigErrorComponent |
            ApiV1WorkspacesReloadCreateK8SAddonsEnabledErrorComponent | ApiV1WorkspacesReloadCreateKindErrorComponent |
            ApiV1WorkspacesReloadCreateLabelsErrorComponent | ApiV1WorkspacesReloadCreateLogsEnabledErrorComponent |
            ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponent |
            ApiV1WorkspacesReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesReloadCreateNameErrorComponent | ApiV1WorkspacesReloadCreateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponent |
            ApiV1WorkspacesReloadCreateOnPremiseErrorComponent | ApiV1WorkspacesReloadCreateOrganizationIdErrorComponent |
            ApiV1WorkspacesReloadCreateOwnerIdErrorComponent | ApiV1WorkspacesReloadCreatePlatformServiceErrorComponent |
            ApiV1WorkspacesReloadCreatePopIdErrorComponent | ApiV1WorkspacesReloadCreateProviderErrorComponent |
            ApiV1WorkspacesReloadCreateProviderIdErrorComponent | ApiV1WorkspacesReloadCreateProviderReferenceErrorComponent
            | ApiV1WorkspacesReloadCreatePurposeErrorComponent | ApiV1WorkspacesReloadCreateReadmeMdErrorComponent |
            ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponent | ApiV1WorkspacesReloadCreateScopeErrorComponent
            | ApiV1WorkspacesReloadCreateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesReloadCreateSlaAvailabilityErrorComponent | ApiV1WorkspacesReloadCreateSlaTargetErrorComponent |
            ApiV1WorkspacesReloadCreateSloAvailabilityErrorComponent | ApiV1WorkspacesReloadCreateSloTargetErrorComponent |
            ApiV1WorkspacesReloadCreateTargetAvailabilityErrorComponent | ApiV1WorkspacesReloadCreateTemplateErrorComponent
            | ApiV1WorkspacesReloadCreateUrlsErrorComponent |
            ApiV1WorkspacesReloadCreateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesReloadCreateActualAvailabilityErrorComponent
        | ApiV1WorkspacesReloadCreateAlternativeNameErrorComponent
        | ApiV1WorkspacesReloadCreateAnnotationsErrorComponent
        | ApiV1WorkspacesReloadCreateArchivedAtErrorComponent
        | ApiV1WorkspacesReloadCreateArchivedErrorComponent
        | ApiV1WorkspacesReloadCreateArchivedReasonErrorComponent
        | ApiV1WorkspacesReloadCreateBackupEnabledErrorComponent
        | ApiV1WorkspacesReloadCreateCriticalityErrorComponent
        | ApiV1WorkspacesReloadCreateDebugModeErrorComponent
        | ApiV1WorkspacesReloadCreateDescriptionErrorComponent
        | ApiV1WorkspacesReloadCreateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesReloadCreateDisplayNameErrorComponent
        | ApiV1WorkspacesReloadCreateEncryptedErrorComponent
        | ApiV1WorkspacesReloadCreateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesReloadCreateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesReloadCreateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesReloadCreateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesReloadCreateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesReloadCreateK8SAddonsEnabledErrorComponent
        | ApiV1WorkspacesReloadCreateKindErrorComponent
        | ApiV1WorkspacesReloadCreateLabelsErrorComponent
        | ApiV1WorkspacesReloadCreateLogsEnabledErrorComponent
        | ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponent
        | ApiV1WorkspacesReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesReloadCreateNameErrorComponent
        | ApiV1WorkspacesReloadCreateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesReloadCreateOnPremiseErrorComponent
        | ApiV1WorkspacesReloadCreateOrganizationIdErrorComponent
        | ApiV1WorkspacesReloadCreateOwnerIdErrorComponent
        | ApiV1WorkspacesReloadCreatePlatformServiceErrorComponent
        | ApiV1WorkspacesReloadCreatePopIdErrorComponent
        | ApiV1WorkspacesReloadCreateProviderErrorComponent
        | ApiV1WorkspacesReloadCreateProviderIdErrorComponent
        | ApiV1WorkspacesReloadCreateProviderReferenceErrorComponent
        | ApiV1WorkspacesReloadCreatePurposeErrorComponent
        | ApiV1WorkspacesReloadCreateReadmeMdErrorComponent
        | ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesReloadCreateScopeErrorComponent
        | ApiV1WorkspacesReloadCreateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesReloadCreateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesReloadCreateSlaTargetErrorComponent
        | ApiV1WorkspacesReloadCreateSloAvailabilityErrorComponent
        | ApiV1WorkspacesReloadCreateSloTargetErrorComponent
        | ApiV1WorkspacesReloadCreateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesReloadCreateTemplateErrorComponent
        | ApiV1WorkspacesReloadCreateUrlsErrorComponent
        | ApiV1WorkspacesReloadCreateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_reload_create_actual_availability_error_component import (
            ApiV1WorkspacesReloadCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_annotations_error_component import (
            ApiV1WorkspacesReloadCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_archived_at_error_component import (
            ApiV1WorkspacesReloadCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_archived_error_component import (
            ApiV1WorkspacesReloadCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_archived_reason_error_component import (
            ApiV1WorkspacesReloadCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_backup_enabled_error_component import (
            ApiV1WorkspacesReloadCreateBackupEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_criticality_error_component import (
            ApiV1WorkspacesReloadCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_debug_mode_error_component import (
            ApiV1WorkspacesReloadCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_description_error_component import (
            ApiV1WorkspacesReloadCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_discovery_enabled_error_component import (
            ApiV1WorkspacesReloadCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_display_name_error_component import (
            ApiV1WorkspacesReloadCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_encrypted_error_component import (
            ApiV1WorkspacesReloadCreateEncryptedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesReloadCreateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesReloadCreateEndpointMonitorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesReloadCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesReloadCreateGlobalEndpointMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesReloadCreateHasIncompatibleKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_k8s_addons_enabled_error_component import (
            ApiV1WorkspacesReloadCreateK8SAddonsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_kind_error_component import (
            ApiV1WorkspacesReloadCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_labels_error_component import (
            ApiV1WorkspacesReloadCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_logs_enabled_error_component import (
            ApiV1WorkspacesReloadCreateLogsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_metrics_enabled_error_component import (
            ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_name_error_component import (
            ApiV1WorkspacesReloadCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_non_field_errors_error_component import (
            ApiV1WorkspacesReloadCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_notifications_enabled_error_component import (
            ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_on_premise_error_component import (
            ApiV1WorkspacesReloadCreateOnPremiseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_organization_id_error_component import (
            ApiV1WorkspacesReloadCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_owner_id_error_component import (
            ApiV1WorkspacesReloadCreateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_platform_service_error_component import (
            ApiV1WorkspacesReloadCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_pop_id_error_component import (
            ApiV1WorkspacesReloadCreatePopIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_provider_error_component import (
            ApiV1WorkspacesReloadCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_provider_id_error_component import (
            ApiV1WorkspacesReloadCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_provider_reference_error_component import (
            ApiV1WorkspacesReloadCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_purpose_error_component import (
            ApiV1WorkspacesReloadCreatePurposeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_readme_md_error_component import (
            ApiV1WorkspacesReloadCreateReadmeMdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_scope_error_component import (
            ApiV1WorkspacesReloadCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesReloadCreateSecretsPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_sla_availability_error_component import (
            ApiV1WorkspacesReloadCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_sla_target_error_component import (
            ApiV1WorkspacesReloadCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_slo_availability_error_component import (
            ApiV1WorkspacesReloadCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_slo_target_error_component import (
            ApiV1WorkspacesReloadCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_target_availability_error_component import (
            ApiV1WorkspacesReloadCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_template_error_component import (
            ApiV1WorkspacesReloadCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_urls_error_component import (
            ApiV1WorkspacesReloadCreateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesReloadCreateWorkspaceInventoryRawErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesReloadCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateLogsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateK8SAddonsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesReloadCreateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_reload_create_actual_availability_error_component import (
            ApiV1WorkspacesReloadCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_alternative_name_error_component import (
            ApiV1WorkspacesReloadCreateAlternativeNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_annotations_error_component import (
            ApiV1WorkspacesReloadCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_archived_at_error_component import (
            ApiV1WorkspacesReloadCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_archived_error_component import (
            ApiV1WorkspacesReloadCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_archived_reason_error_component import (
            ApiV1WorkspacesReloadCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_backup_enabled_error_component import (
            ApiV1WorkspacesReloadCreateBackupEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_criticality_error_component import (
            ApiV1WorkspacesReloadCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_debug_mode_error_component import (
            ApiV1WorkspacesReloadCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_description_error_component import (
            ApiV1WorkspacesReloadCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_discovery_enabled_error_component import (
            ApiV1WorkspacesReloadCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_display_name_error_component import (
            ApiV1WorkspacesReloadCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_encrypted_error_component import (
            ApiV1WorkspacesReloadCreateEncryptedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesReloadCreateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesReloadCreateEndpointMonitorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesReloadCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesReloadCreateGlobalEndpointMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesReloadCreateHasIncompatibleKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_k8s_addons_enabled_error_component import (
            ApiV1WorkspacesReloadCreateK8SAddonsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_kind_error_component import (
            ApiV1WorkspacesReloadCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_labels_error_component import (
            ApiV1WorkspacesReloadCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_logs_enabled_error_component import (
            ApiV1WorkspacesReloadCreateLogsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_metrics_enabled_error_component import (
            ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_name_error_component import (
            ApiV1WorkspacesReloadCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_non_field_errors_error_component import (
            ApiV1WorkspacesReloadCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_notifications_enabled_error_component import (
            ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_on_premise_error_component import (
            ApiV1WorkspacesReloadCreateOnPremiseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_organization_id_error_component import (
            ApiV1WorkspacesReloadCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_owner_id_error_component import (
            ApiV1WorkspacesReloadCreateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_platform_service_error_component import (
            ApiV1WorkspacesReloadCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_pop_id_error_component import (
            ApiV1WorkspacesReloadCreatePopIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_provider_error_component import (
            ApiV1WorkspacesReloadCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_provider_id_error_component import (
            ApiV1WorkspacesReloadCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_provider_reference_error_component import (
            ApiV1WorkspacesReloadCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_purpose_error_component import (
            ApiV1WorkspacesReloadCreatePurposeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_readme_md_error_component import (
            ApiV1WorkspacesReloadCreateReadmeMdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_scope_error_component import (
            ApiV1WorkspacesReloadCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesReloadCreateSecretsPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_sla_availability_error_component import (
            ApiV1WorkspacesReloadCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_sla_target_error_component import (
            ApiV1WorkspacesReloadCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_slo_availability_error_component import (
            ApiV1WorkspacesReloadCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_slo_target_error_component import (
            ApiV1WorkspacesReloadCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_target_availability_error_component import (
            ApiV1WorkspacesReloadCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_template_error_component import (
            ApiV1WorkspacesReloadCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_urls_error_component import (
            ApiV1WorkspacesReloadCreateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspaces_reload_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesReloadCreateWorkspaceInventoryRawErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesReloadCreateActualAvailabilityErrorComponent
                | ApiV1WorkspacesReloadCreateAlternativeNameErrorComponent
                | ApiV1WorkspacesReloadCreateAnnotationsErrorComponent
                | ApiV1WorkspacesReloadCreateArchivedAtErrorComponent
                | ApiV1WorkspacesReloadCreateArchivedErrorComponent
                | ApiV1WorkspacesReloadCreateArchivedReasonErrorComponent
                | ApiV1WorkspacesReloadCreateBackupEnabledErrorComponent
                | ApiV1WorkspacesReloadCreateCriticalityErrorComponent
                | ApiV1WorkspacesReloadCreateDebugModeErrorComponent
                | ApiV1WorkspacesReloadCreateDescriptionErrorComponent
                | ApiV1WorkspacesReloadCreateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesReloadCreateDisplayNameErrorComponent
                | ApiV1WorkspacesReloadCreateEncryptedErrorComponent
                | ApiV1WorkspacesReloadCreateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesReloadCreateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesReloadCreateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesReloadCreateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesReloadCreateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesReloadCreateK8SAddonsEnabledErrorComponent
                | ApiV1WorkspacesReloadCreateKindErrorComponent
                | ApiV1WorkspacesReloadCreateLabelsErrorComponent
                | ApiV1WorkspacesReloadCreateLogsEnabledErrorComponent
                | ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponent
                | ApiV1WorkspacesReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesReloadCreateNameErrorComponent
                | ApiV1WorkspacesReloadCreateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesReloadCreateOnPremiseErrorComponent
                | ApiV1WorkspacesReloadCreateOrganizationIdErrorComponent
                | ApiV1WorkspacesReloadCreateOwnerIdErrorComponent
                | ApiV1WorkspacesReloadCreatePlatformServiceErrorComponent
                | ApiV1WorkspacesReloadCreatePopIdErrorComponent
                | ApiV1WorkspacesReloadCreateProviderErrorComponent
                | ApiV1WorkspacesReloadCreateProviderIdErrorComponent
                | ApiV1WorkspacesReloadCreateProviderReferenceErrorComponent
                | ApiV1WorkspacesReloadCreatePurposeErrorComponent
                | ApiV1WorkspacesReloadCreateReadmeMdErrorComponent
                | ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesReloadCreateScopeErrorComponent
                | ApiV1WorkspacesReloadCreateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesReloadCreateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesReloadCreateSlaTargetErrorComponent
                | ApiV1WorkspacesReloadCreateSloAvailabilityErrorComponent
                | ApiV1WorkspacesReloadCreateSloTargetErrorComponent
                | ApiV1WorkspacesReloadCreateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesReloadCreateTemplateErrorComponent
                | ApiV1WorkspacesReloadCreateUrlsErrorComponent
                | ApiV1WorkspacesReloadCreateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_0 = (
                        ApiV1WorkspacesReloadCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_1 = (
                        ApiV1WorkspacesReloadCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_2 = (
                        ApiV1WorkspacesReloadCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_3 = (
                        ApiV1WorkspacesReloadCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_4 = (
                        ApiV1WorkspacesReloadCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_5 = (
                        ApiV1WorkspacesReloadCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_6 = (
                        ApiV1WorkspacesReloadCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_7 = (
                        ApiV1WorkspacesReloadCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_8 = (
                        ApiV1WorkspacesReloadCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_9 = (
                        ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_10 = (
                        ApiV1WorkspacesReloadCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_11 = (
                        ApiV1WorkspacesReloadCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_12 = (
                        ApiV1WorkspacesReloadCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_13 = (
                        ApiV1WorkspacesReloadCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_14 = (
                        ApiV1WorkspacesReloadCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_15 = (
                        ApiV1WorkspacesReloadCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_16 = (
                        ApiV1WorkspacesReloadCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_17 = (
                        ApiV1WorkspacesReloadCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_18 = (
                        ApiV1WorkspacesReloadCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_19 = (
                        ApiV1WorkspacesReloadCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_20 = (
                        ApiV1WorkspacesReloadCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_21 = (
                        ApiV1WorkspacesReloadCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_22 = (
                        ApiV1WorkspacesReloadCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_23 = (
                        ApiV1WorkspacesReloadCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_24 = (
                        ApiV1WorkspacesReloadCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_25 = (
                        ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_26 = (
                        ApiV1WorkspacesReloadCreateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_27 = (
                        ApiV1WorkspacesReloadCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_28 = (
                        ApiV1WorkspacesReloadCreateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_29 = (
                        ApiV1WorkspacesReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_30 = (
                        ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_31 = (
                        ApiV1WorkspacesReloadCreateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_32 = (
                        ApiV1WorkspacesReloadCreateMetricsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_33 = (
                        ApiV1WorkspacesReloadCreateLogsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_34 = (
                        ApiV1WorkspacesReloadCreateK8SAddonsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_35 = (
                        ApiV1WorkspacesReloadCreateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_36 = (
                        ApiV1WorkspacesReloadCreateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_37 = (
                        ApiV1WorkspacesReloadCreateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_38 = (
                        ApiV1WorkspacesReloadCreateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_39 = (
                        ApiV1WorkspacesReloadCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_40 = (
                        ApiV1WorkspacesReloadCreateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_41 = (
                        ApiV1WorkspacesReloadCreatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_42 = (
                        ApiV1WorkspacesReloadCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_43 = (
                        ApiV1WorkspacesReloadCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_44 = (
                        ApiV1WorkspacesReloadCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_45 = (
                        ApiV1WorkspacesReloadCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_46 = (
                        ApiV1WorkspacesReloadCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_reload_create_error_type_47 = (
                        ApiV1WorkspacesReloadCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_reload_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_reload_create_error_type_48 = (
                    ApiV1WorkspacesReloadCreateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_reload_create_error_type_48

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_reload_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_reload_create_validation_error.additional_properties = d
        return api_v1_workspaces_reload_create_validation_error

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
