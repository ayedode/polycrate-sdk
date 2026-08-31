from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_clusters_partial_update_active_error_component import (
        ApiV1KubernetesClustersPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_actual_availability_error_component import (
        ApiV1KubernetesClustersPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_addons_error_component import (
        ApiV1KubernetesClustersPartialUpdateAddonsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_alias_error_component import (
        ApiV1KubernetesClustersPartialUpdateAliasErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_annotations_error_component import (
        ApiV1KubernetesClustersPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_api_server_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersPartialUpdateApiServerCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_archived_at_error_component import (
        ApiV1KubernetesClustersPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_archived_error_component import (
        ApiV1KubernetesClustersPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_archived_reason_error_component import (
        ApiV1KubernetesClustersPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_backup_schedules_error_component import (
        ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_baserow_id_error_component import (
        ApiV1KubernetesClustersPartialUpdateBaserowIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_credential_error_component import (
        ApiV1KubernetesClustersPartialUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_criticality_error_component import (
        ApiV1KubernetesClustersPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_debug_mode_error_component import (
        ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_description_error_component import (
        ApiV1KubernetesClustersPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_discovery_enabled_error_component import (
        ApiV1KubernetesClustersPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_discovery_ignored_namespaces_error_component import (
        ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_display_name_error_component import (
        ApiV1KubernetesClustersPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_gitlab_project_id_error_component import (
        ApiV1KubernetesClustersPartialUpdateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_installed_error_component import (
        ApiV1KubernetesClustersPartialUpdateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_is_host_cluster_error_component import (
        ApiV1KubernetesClustersPartialUpdateIsHostClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_is_infrastructure_cluster_error_component import (
        ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_kind_error_component import (
        ApiV1KubernetesClustersPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_kubeconfig_ca_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersPartialUpdateKubeconfigCaCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_kubeconfig_client_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersPartialUpdateKubeconfigClientCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_kubernetes_version_error_component import (
        ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_labels_error_component import (
        ApiV1KubernetesClustersPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_last_backup_import_error_component import (
        ApiV1KubernetesClustersPartialUpdateLastBackupImportErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_managed_by_content_type_error_component import (
        ApiV1KubernetesClustersPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_managed_by_object_id_error_component import (
        ApiV1KubernetesClustersPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_name_error_component import (
        ApiV1KubernetesClustersPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_non_field_errors_error_component import (
        ApiV1KubernetesClustersPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_operator_ignore_namespaces_error_component import (
        ApiV1KubernetesClustersPartialUpdateOperatorIgnoreNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_operator_loglevel_error_component import (
        ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_platform_dns_record_created_error_component import (
        ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_platform_service_error_component import (
        ApiV1KubernetesClustersPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_provider_error_component import (
        ApiV1KubernetesClustersPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_provider_id_error_component import (
        ApiV1KubernetesClustersPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_provider_reference_error_component import (
        ApiV1KubernetesClustersPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesClustersPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_scope_error_component import (
        ApiV1KubernetesClustersPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_sla_availability_error_component import (
        ApiV1KubernetesClustersPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_sla_target_error_component import (
        ApiV1KubernetesClustersPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_slo_availability_error_component import (
        ApiV1KubernetesClustersPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_slo_target_error_component import (
        ApiV1KubernetesClustersPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_slug_error_component import (
        ApiV1KubernetesClustersPartialUpdateSlugErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_partial_update_target_availability_error_component import (
        ApiV1KubernetesClustersPartialUpdateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClustersPartialUpdateValidationError")


@_attrs_define
class ApiV1KubernetesClustersPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClustersPartialUpdateActiveErrorComponent |
            ApiV1KubernetesClustersPartialUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesClustersPartialUpdateAddonsErrorComponent |
            ApiV1KubernetesClustersPartialUpdateAliasErrorComponent |
            ApiV1KubernetesClustersPartialUpdateAnnotationsErrorComponent |
            ApiV1KubernetesClustersPartialUpdateApiServerCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersPartialUpdateArchivedAtErrorComponent |
            ApiV1KubernetesClustersPartialUpdateArchivedErrorComponent |
            ApiV1KubernetesClustersPartialUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponent |
            ApiV1KubernetesClustersPartialUpdateBaserowIdErrorComponent |
            ApiV1KubernetesClustersPartialUpdateCredentialErrorComponent |
            ApiV1KubernetesClustersPartialUpdateCriticalityErrorComponent |
            ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponent |
            ApiV1KubernetesClustersPartialUpdateDescriptionErrorComponent |
            ApiV1KubernetesClustersPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponent |
            ApiV1KubernetesClustersPartialUpdateDisplayNameErrorComponent |
            ApiV1KubernetesClustersPartialUpdateGitlabProjectIdErrorComponent |
            ApiV1KubernetesClustersPartialUpdateInstalledErrorComponent |
            ApiV1KubernetesClustersPartialUpdateIsHostClusterErrorComponent |
            ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponent |
            ApiV1KubernetesClustersPartialUpdateKindErrorComponent |
            ApiV1KubernetesClustersPartialUpdateKubeconfigCaCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersPartialUpdateKubeconfigClientCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponent |
            ApiV1KubernetesClustersPartialUpdateLabelsErrorComponent |
            ApiV1KubernetesClustersPartialUpdateLastBackupImportErrorComponent |
            ApiV1KubernetesClustersPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1KubernetesClustersPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1KubernetesClustersPartialUpdateNameErrorComponent |
            ApiV1KubernetesClustersPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClustersPartialUpdateOperatorIgnoreNamespacesErrorComponent |
            ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponent |
            ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesClustersPartialUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesClustersPartialUpdateProviderErrorComponent |
            ApiV1KubernetesClustersPartialUpdateProviderIdErrorComponent |
            ApiV1KubernetesClustersPartialUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesClustersPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClustersPartialUpdateScopeErrorComponent |
            ApiV1KubernetesClustersPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClustersPartialUpdateSlaTargetErrorComponent |
            ApiV1KubernetesClustersPartialUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesClustersPartialUpdateSloTargetErrorComponent |
            ApiV1KubernetesClustersPartialUpdateSlugErrorComponent |
            ApiV1KubernetesClustersPartialUpdateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClustersPartialUpdateActiveErrorComponent
        | ApiV1KubernetesClustersPartialUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesClustersPartialUpdateAddonsErrorComponent
        | ApiV1KubernetesClustersPartialUpdateAliasErrorComponent
        | ApiV1KubernetesClustersPartialUpdateAnnotationsErrorComponent
        | ApiV1KubernetesClustersPartialUpdateApiServerCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersPartialUpdateArchivedAtErrorComponent
        | ApiV1KubernetesClustersPartialUpdateArchivedErrorComponent
        | ApiV1KubernetesClustersPartialUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponent
        | ApiV1KubernetesClustersPartialUpdateBaserowIdErrorComponent
        | ApiV1KubernetesClustersPartialUpdateCredentialErrorComponent
        | ApiV1KubernetesClustersPartialUpdateCriticalityErrorComponent
        | ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponent
        | ApiV1KubernetesClustersPartialUpdateDescriptionErrorComponent
        | ApiV1KubernetesClustersPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponent
        | ApiV1KubernetesClustersPartialUpdateDisplayNameErrorComponent
        | ApiV1KubernetesClustersPartialUpdateGitlabProjectIdErrorComponent
        | ApiV1KubernetesClustersPartialUpdateInstalledErrorComponent
        | ApiV1KubernetesClustersPartialUpdateIsHostClusterErrorComponent
        | ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponent
        | ApiV1KubernetesClustersPartialUpdateKindErrorComponent
        | ApiV1KubernetesClustersPartialUpdateKubeconfigCaCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersPartialUpdateKubeconfigClientCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponent
        | ApiV1KubernetesClustersPartialUpdateLabelsErrorComponent
        | ApiV1KubernetesClustersPartialUpdateLastBackupImportErrorComponent
        | ApiV1KubernetesClustersPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1KubernetesClustersPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1KubernetesClustersPartialUpdateNameErrorComponent
        | ApiV1KubernetesClustersPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClustersPartialUpdateOperatorIgnoreNamespacesErrorComponent
        | ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponent
        | ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesClustersPartialUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesClustersPartialUpdateProviderErrorComponent
        | ApiV1KubernetesClustersPartialUpdateProviderIdErrorComponent
        | ApiV1KubernetesClustersPartialUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesClustersPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClustersPartialUpdateScopeErrorComponent
        | ApiV1KubernetesClustersPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClustersPartialUpdateSlaTargetErrorComponent
        | ApiV1KubernetesClustersPartialUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesClustersPartialUpdateSloTargetErrorComponent
        | ApiV1KubernetesClustersPartialUpdateSlugErrorComponent
        | ApiV1KubernetesClustersPartialUpdateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_clusters_partial_update_active_error_component import (
            ApiV1KubernetesClustersPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_actual_availability_error_component import (
            ApiV1KubernetesClustersPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_addons_error_component import (
            ApiV1KubernetesClustersPartialUpdateAddonsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_alias_error_component import (
            ApiV1KubernetesClustersPartialUpdateAliasErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_annotations_error_component import (
            ApiV1KubernetesClustersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersPartialUpdateApiServerCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_archived_at_error_component import (
            ApiV1KubernetesClustersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_archived_error_component import (
            ApiV1KubernetesClustersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_archived_reason_error_component import (
            ApiV1KubernetesClustersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_backup_schedules_error_component import (
            ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_baserow_id_error_component import (
            ApiV1KubernetesClustersPartialUpdateBaserowIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_credential_error_component import (
            ApiV1KubernetesClustersPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_criticality_error_component import (
            ApiV1KubernetesClustersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_debug_mode_error_component import (
            ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_description_error_component import (
            ApiV1KubernetesClustersPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesClustersPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_display_name_error_component import (
            ApiV1KubernetesClustersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersPartialUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_installed_error_component import (
            ApiV1KubernetesClustersPartialUpdateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_is_host_cluster_error_component import (
            ApiV1KubernetesClustersPartialUpdateIsHostClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_kind_error_component import (
            ApiV1KubernetesClustersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersPartialUpdateKubeconfigCaCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersPartialUpdateKubeconfigClientCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_kubernetes_version_error_component import (
            ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_labels_error_component import (
            ApiV1KubernetesClustersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_last_backup_import_error_component import (
            ApiV1KubernetesClustersPartialUpdateLastBackupImportErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_name_error_component import (
            ApiV1KubernetesClustersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesClustersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersPartialUpdateOperatorIgnoreNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_operator_loglevel_error_component import (
            ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_platform_service_error_component import (
            ApiV1KubernetesClustersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_provider_error_component import (
            ApiV1KubernetesClustersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_provider_id_error_component import (
            ApiV1KubernetesClustersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_provider_reference_error_component import (
            ApiV1KubernetesClustersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_scope_error_component import (
            ApiV1KubernetesClustersPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_sla_availability_error_component import (
            ApiV1KubernetesClustersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_sla_target_error_component import (
            ApiV1KubernetesClustersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_slo_availability_error_component import (
            ApiV1KubernetesClustersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_slo_target_error_component import (
            ApiV1KubernetesClustersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_slug_error_component import (
            ApiV1KubernetesClustersPartialUpdateSlugErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_target_availability_error_component import (
            ApiV1KubernetesClustersPartialUpdateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateIsHostClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersPartialUpdateKubeconfigCaCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersPartialUpdateKubeconfigClientCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersPartialUpdateApiServerCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersPartialUpdateOperatorIgnoreNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateAddonsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateBaserowIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateLastBackupImportErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersPartialUpdateManagedByContentTypeErrorComponent):
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
        from ..models.api_v1_kubernetes_clusters_partial_update_active_error_component import (
            ApiV1KubernetesClustersPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_actual_availability_error_component import (
            ApiV1KubernetesClustersPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_addons_error_component import (
            ApiV1KubernetesClustersPartialUpdateAddonsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_alias_error_component import (
            ApiV1KubernetesClustersPartialUpdateAliasErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_annotations_error_component import (
            ApiV1KubernetesClustersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersPartialUpdateApiServerCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_archived_at_error_component import (
            ApiV1KubernetesClustersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_archived_error_component import (
            ApiV1KubernetesClustersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_archived_reason_error_component import (
            ApiV1KubernetesClustersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_backup_schedules_error_component import (
            ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_baserow_id_error_component import (
            ApiV1KubernetesClustersPartialUpdateBaserowIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_credential_error_component import (
            ApiV1KubernetesClustersPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_criticality_error_component import (
            ApiV1KubernetesClustersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_debug_mode_error_component import (
            ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_description_error_component import (
            ApiV1KubernetesClustersPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesClustersPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_display_name_error_component import (
            ApiV1KubernetesClustersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersPartialUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_installed_error_component import (
            ApiV1KubernetesClustersPartialUpdateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_is_host_cluster_error_component import (
            ApiV1KubernetesClustersPartialUpdateIsHostClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_kind_error_component import (
            ApiV1KubernetesClustersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersPartialUpdateKubeconfigCaCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersPartialUpdateKubeconfigClientCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_kubernetes_version_error_component import (
            ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_labels_error_component import (
            ApiV1KubernetesClustersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_last_backup_import_error_component import (
            ApiV1KubernetesClustersPartialUpdateLastBackupImportErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_managed_by_object_id_error_component import (
            ApiV1KubernetesClustersPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_name_error_component import (
            ApiV1KubernetesClustersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesClustersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersPartialUpdateOperatorIgnoreNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_operator_loglevel_error_component import (
            ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_platform_service_error_component import (
            ApiV1KubernetesClustersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_provider_error_component import (
            ApiV1KubernetesClustersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_provider_id_error_component import (
            ApiV1KubernetesClustersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_provider_reference_error_component import (
            ApiV1KubernetesClustersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_scope_error_component import (
            ApiV1KubernetesClustersPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_sla_availability_error_component import (
            ApiV1KubernetesClustersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_sla_target_error_component import (
            ApiV1KubernetesClustersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_slo_availability_error_component import (
            ApiV1KubernetesClustersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_slo_target_error_component import (
            ApiV1KubernetesClustersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_slug_error_component import (
            ApiV1KubernetesClustersPartialUpdateSlugErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_partial_update_target_availability_error_component import (
            ApiV1KubernetesClustersPartialUpdateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClustersPartialUpdateActiveErrorComponent
                | ApiV1KubernetesClustersPartialUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesClustersPartialUpdateAddonsErrorComponent
                | ApiV1KubernetesClustersPartialUpdateAliasErrorComponent
                | ApiV1KubernetesClustersPartialUpdateAnnotationsErrorComponent
                | ApiV1KubernetesClustersPartialUpdateApiServerCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersPartialUpdateArchivedAtErrorComponent
                | ApiV1KubernetesClustersPartialUpdateArchivedErrorComponent
                | ApiV1KubernetesClustersPartialUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponent
                | ApiV1KubernetesClustersPartialUpdateBaserowIdErrorComponent
                | ApiV1KubernetesClustersPartialUpdateCredentialErrorComponent
                | ApiV1KubernetesClustersPartialUpdateCriticalityErrorComponent
                | ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponent
                | ApiV1KubernetesClustersPartialUpdateDescriptionErrorComponent
                | ApiV1KubernetesClustersPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponent
                | ApiV1KubernetesClustersPartialUpdateDisplayNameErrorComponent
                | ApiV1KubernetesClustersPartialUpdateGitlabProjectIdErrorComponent
                | ApiV1KubernetesClustersPartialUpdateInstalledErrorComponent
                | ApiV1KubernetesClustersPartialUpdateIsHostClusterErrorComponent
                | ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponent
                | ApiV1KubernetesClustersPartialUpdateKindErrorComponent
                | ApiV1KubernetesClustersPartialUpdateKubeconfigCaCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersPartialUpdateKubeconfigClientCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponent
                | ApiV1KubernetesClustersPartialUpdateLabelsErrorComponent
                | ApiV1KubernetesClustersPartialUpdateLastBackupImportErrorComponent
                | ApiV1KubernetesClustersPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1KubernetesClustersPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1KubernetesClustersPartialUpdateNameErrorComponent
                | ApiV1KubernetesClustersPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClustersPartialUpdateOperatorIgnoreNamespacesErrorComponent
                | ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponent
                | ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesClustersPartialUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesClustersPartialUpdateProviderErrorComponent
                | ApiV1KubernetesClustersPartialUpdateProviderIdErrorComponent
                | ApiV1KubernetesClustersPartialUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesClustersPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClustersPartialUpdateScopeErrorComponent
                | ApiV1KubernetesClustersPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClustersPartialUpdateSlaTargetErrorComponent
                | ApiV1KubernetesClustersPartialUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesClustersPartialUpdateSloTargetErrorComponent
                | ApiV1KubernetesClustersPartialUpdateSlugErrorComponent
                | ApiV1KubernetesClustersPartialUpdateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_0 = (
                        ApiV1KubernetesClustersPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_1 = (
                        ApiV1KubernetesClustersPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_2 = (
                        ApiV1KubernetesClustersPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_3 = (
                        ApiV1KubernetesClustersPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_4 = (
                        ApiV1KubernetesClustersPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_5 = (
                        ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_6 = (
                        ApiV1KubernetesClustersPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_7 = (
                        ApiV1KubernetesClustersPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_8 = (
                        ApiV1KubernetesClustersPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_9 = (
                        ApiV1KubernetesClustersPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_10 = (
                        ApiV1KubernetesClustersPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_11 = (
                        ApiV1KubernetesClustersPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_12 = (
                        ApiV1KubernetesClustersPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_13 = (
                        ApiV1KubernetesClustersPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_14 = (
                        ApiV1KubernetesClustersPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_15 = (
                        ApiV1KubernetesClustersPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_16 = (
                        ApiV1KubernetesClustersPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_17 = (
                        ApiV1KubernetesClustersPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_18 = (
                        ApiV1KubernetesClustersPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_19 = (
                        ApiV1KubernetesClustersPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_20 = (
                        ApiV1KubernetesClustersPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_21 = (
                        ApiV1KubernetesClustersPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_22 = (
                        ApiV1KubernetesClustersPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_23 = (
                        ApiV1KubernetesClustersPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_24 = (
                        ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_25 = (
                        ApiV1KubernetesClustersPartialUpdateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_26 = (
                        ApiV1KubernetesClustersPartialUpdateIsHostClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_27 = (
                        ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_28 = (
                        ApiV1KubernetesClustersPartialUpdateKubeconfigCaCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_29 = (
                        ApiV1KubernetesClustersPartialUpdateKubeconfigClientCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_30 = (
                        ApiV1KubernetesClustersPartialUpdateApiServerCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_31 = (
                        ApiV1KubernetesClustersPartialUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_32 = (
                        ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_33 = (
                        ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_34 = (
                        ApiV1KubernetesClustersPartialUpdateOperatorIgnoreNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_35 = (
                        ApiV1KubernetesClustersPartialUpdateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_36 = (
                        ApiV1KubernetesClustersPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_37 = (
                        ApiV1KubernetesClustersPartialUpdateAddonsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_38 = (
                        ApiV1KubernetesClustersPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_39 = (
                        ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_40 = (
                        ApiV1KubernetesClustersPartialUpdateBaserowIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_41 = (
                        ApiV1KubernetesClustersPartialUpdateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_42 = (
                        ApiV1KubernetesClustersPartialUpdateLastBackupImportErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_43 = (
                        ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_44 = (
                        ApiV1KubernetesClustersPartialUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_45 = (
                        ApiV1KubernetesClustersPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_46 = (
                    ApiV1KubernetesClustersPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_clusters_partial_update_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_clusters_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_clusters_partial_update_validation_error.additional_properties = d
        return api_v1_kubernetes_clusters_partial_update_validation_error

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
