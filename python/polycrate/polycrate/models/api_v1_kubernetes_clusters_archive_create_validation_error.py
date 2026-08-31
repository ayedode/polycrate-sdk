from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_clusters_archive_create_active_error_component import (
        ApiV1KubernetesClustersArchiveCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_actual_availability_error_component import (
        ApiV1KubernetesClustersArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_addons_error_component import (
        ApiV1KubernetesClustersArchiveCreateAddonsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_alias_error_component import (
        ApiV1KubernetesClustersArchiveCreateAliasErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_annotations_error_component import (
        ApiV1KubernetesClustersArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_api_server_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersArchiveCreateApiServerCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_archived_at_error_component import (
        ApiV1KubernetesClustersArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_archived_error_component import (
        ApiV1KubernetesClustersArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_archived_reason_error_component import (
        ApiV1KubernetesClustersArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_backup_schedules_error_component import (
        ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_baserow_id_error_component import (
        ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_credential_error_component import (
        ApiV1KubernetesClustersArchiveCreateCredentialErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_criticality_error_component import (
        ApiV1KubernetesClustersArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_debug_mode_error_component import (
        ApiV1KubernetesClustersArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_description_error_component import (
        ApiV1KubernetesClustersArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_discovery_enabled_error_component import (
        ApiV1KubernetesClustersArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_discovery_ignored_namespaces_error_component import (
        ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_display_name_error_component import (
        ApiV1KubernetesClustersArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_gitlab_project_id_error_component import (
        ApiV1KubernetesClustersArchiveCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_installed_error_component import (
        ApiV1KubernetesClustersArchiveCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_is_host_cluster_error_component import (
        ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_is_infrastructure_cluster_error_component import (
        ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_kind_error_component import (
        ApiV1KubernetesClustersArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_kubeconfig_ca_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersArchiveCreateKubeconfigCaCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_kubeconfig_client_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersArchiveCreateKubeconfigClientCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_kubernetes_version_error_component import (
        ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_labels_error_component import (
        ApiV1KubernetesClustersArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_last_backup_import_error_component import (
        ApiV1KubernetesClustersArchiveCreateLastBackupImportErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_managed_by_content_type_error_component import (
        ApiV1KubernetesClustersArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_managed_by_object_id_error_component import (
        ApiV1KubernetesClustersArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_name_error_component import (
        ApiV1KubernetesClustersArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_non_field_errors_error_component import (
        ApiV1KubernetesClustersArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_operator_ignore_namespaces_error_component import (
        ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_operator_loglevel_error_component import (
        ApiV1KubernetesClustersArchiveCreateOperatorLoglevelErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_platform_service_error_component import (
        ApiV1KubernetesClustersArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_provider_error_component import (
        ApiV1KubernetesClustersArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_provider_id_error_component import (
        ApiV1KubernetesClustersArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_provider_reference_error_component import (
        ApiV1KubernetesClustersArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesClustersArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_scope_error_component import (
        ApiV1KubernetesClustersArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_sla_availability_error_component import (
        ApiV1KubernetesClustersArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_sla_target_error_component import (
        ApiV1KubernetesClustersArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_slo_availability_error_component import (
        ApiV1KubernetesClustersArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_slo_target_error_component import (
        ApiV1KubernetesClustersArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_slug_error_component import (
        ApiV1KubernetesClustersArchiveCreateSlugErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_archive_create_target_availability_error_component import (
        ApiV1KubernetesClustersArchiveCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClustersArchiveCreateValidationError")


@_attrs_define
class ApiV1KubernetesClustersArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClustersArchiveCreateActiveErrorComponent |
            ApiV1KubernetesClustersArchiveCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesClustersArchiveCreateAddonsErrorComponent |
            ApiV1KubernetesClustersArchiveCreateAliasErrorComponent |
            ApiV1KubernetesClustersArchiveCreateAnnotationsErrorComponent |
            ApiV1KubernetesClustersArchiveCreateApiServerCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersArchiveCreateArchivedAtErrorComponent |
            ApiV1KubernetesClustersArchiveCreateArchivedErrorComponent |
            ApiV1KubernetesClustersArchiveCreateArchivedReasonErrorComponent |
            ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponent |
            ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponent |
            ApiV1KubernetesClustersArchiveCreateCredentialErrorComponent |
            ApiV1KubernetesClustersArchiveCreateCriticalityErrorComponent |
            ApiV1KubernetesClustersArchiveCreateDebugModeErrorComponent |
            ApiV1KubernetesClustersArchiveCreateDescriptionErrorComponent |
            ApiV1KubernetesClustersArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponent |
            ApiV1KubernetesClustersArchiveCreateDisplayNameErrorComponent |
            ApiV1KubernetesClustersArchiveCreateGitlabProjectIdErrorComponent |
            ApiV1KubernetesClustersArchiveCreateInstalledErrorComponent |
            ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponent |
            ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponent |
            ApiV1KubernetesClustersArchiveCreateKindErrorComponent |
            ApiV1KubernetesClustersArchiveCreateKubeconfigCaCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersArchiveCreateKubeconfigClientCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponent |
            ApiV1KubernetesClustersArchiveCreateLabelsErrorComponent |
            ApiV1KubernetesClustersArchiveCreateLastBackupImportErrorComponent |
            ApiV1KubernetesClustersArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesClustersArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1KubernetesClustersArchiveCreateNameErrorComponent |
            ApiV1KubernetesClustersArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponent |
            ApiV1KubernetesClustersArchiveCreateOperatorLoglevelErrorComponent |
            ApiV1KubernetesClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesClustersArchiveCreatePlatformServiceErrorComponent |
            ApiV1KubernetesClustersArchiveCreateProviderErrorComponent |
            ApiV1KubernetesClustersArchiveCreateProviderIdErrorComponent |
            ApiV1KubernetesClustersArchiveCreateProviderReferenceErrorComponent |
            ApiV1KubernetesClustersArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClustersArchiveCreateScopeErrorComponent |
            ApiV1KubernetesClustersArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClustersArchiveCreateSlaTargetErrorComponent |
            ApiV1KubernetesClustersArchiveCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesClustersArchiveCreateSloTargetErrorComponent |
            ApiV1KubernetesClustersArchiveCreateSlugErrorComponent |
            ApiV1KubernetesClustersArchiveCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClustersArchiveCreateActiveErrorComponent
        | ApiV1KubernetesClustersArchiveCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesClustersArchiveCreateAddonsErrorComponent
        | ApiV1KubernetesClustersArchiveCreateAliasErrorComponent
        | ApiV1KubernetesClustersArchiveCreateAnnotationsErrorComponent
        | ApiV1KubernetesClustersArchiveCreateApiServerCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersArchiveCreateArchivedAtErrorComponent
        | ApiV1KubernetesClustersArchiveCreateArchivedErrorComponent
        | ApiV1KubernetesClustersArchiveCreateArchivedReasonErrorComponent
        | ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponent
        | ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponent
        | ApiV1KubernetesClustersArchiveCreateCredentialErrorComponent
        | ApiV1KubernetesClustersArchiveCreateCriticalityErrorComponent
        | ApiV1KubernetesClustersArchiveCreateDebugModeErrorComponent
        | ApiV1KubernetesClustersArchiveCreateDescriptionErrorComponent
        | ApiV1KubernetesClustersArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponent
        | ApiV1KubernetesClustersArchiveCreateDisplayNameErrorComponent
        | ApiV1KubernetesClustersArchiveCreateGitlabProjectIdErrorComponent
        | ApiV1KubernetesClustersArchiveCreateInstalledErrorComponent
        | ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponent
        | ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponent
        | ApiV1KubernetesClustersArchiveCreateKindErrorComponent
        | ApiV1KubernetesClustersArchiveCreateKubeconfigCaCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersArchiveCreateKubeconfigClientCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponent
        | ApiV1KubernetesClustersArchiveCreateLabelsErrorComponent
        | ApiV1KubernetesClustersArchiveCreateLastBackupImportErrorComponent
        | ApiV1KubernetesClustersArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesClustersArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesClustersArchiveCreateNameErrorComponent
        | ApiV1KubernetesClustersArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponent
        | ApiV1KubernetesClustersArchiveCreateOperatorLoglevelErrorComponent
        | ApiV1KubernetesClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesClustersArchiveCreatePlatformServiceErrorComponent
        | ApiV1KubernetesClustersArchiveCreateProviderErrorComponent
        | ApiV1KubernetesClustersArchiveCreateProviderIdErrorComponent
        | ApiV1KubernetesClustersArchiveCreateProviderReferenceErrorComponent
        | ApiV1KubernetesClustersArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClustersArchiveCreateScopeErrorComponent
        | ApiV1KubernetesClustersArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClustersArchiveCreateSlaTargetErrorComponent
        | ApiV1KubernetesClustersArchiveCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesClustersArchiveCreateSloTargetErrorComponent
        | ApiV1KubernetesClustersArchiveCreateSlugErrorComponent
        | ApiV1KubernetesClustersArchiveCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_clusters_archive_create_active_error_component import (
            ApiV1KubernetesClustersArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_actual_availability_error_component import (
            ApiV1KubernetesClustersArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_addons_error_component import (
            ApiV1KubernetesClustersArchiveCreateAddonsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_alias_error_component import (
            ApiV1KubernetesClustersArchiveCreateAliasErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_annotations_error_component import (
            ApiV1KubernetesClustersArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersArchiveCreateApiServerCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_archived_at_error_component import (
            ApiV1KubernetesClustersArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_archived_error_component import (
            ApiV1KubernetesClustersArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_archived_reason_error_component import (
            ApiV1KubernetesClustersArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_backup_schedules_error_component import (
            ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_baserow_id_error_component import (
            ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_credential_error_component import (
            ApiV1KubernetesClustersArchiveCreateCredentialErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_criticality_error_component import (
            ApiV1KubernetesClustersArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_debug_mode_error_component import (
            ApiV1KubernetesClustersArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_description_error_component import (
            ApiV1KubernetesClustersArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesClustersArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_display_name_error_component import (
            ApiV1KubernetesClustersArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersArchiveCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_installed_error_component import (
            ApiV1KubernetesClustersArchiveCreateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_is_host_cluster_error_component import (
            ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_kind_error_component import (
            ApiV1KubernetesClustersArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersArchiveCreateKubeconfigCaCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersArchiveCreateKubeconfigClientCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_kubernetes_version_error_component import (
            ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_labels_error_component import (
            ApiV1KubernetesClustersArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_last_backup_import_error_component import (
            ApiV1KubernetesClustersArchiveCreateLastBackupImportErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_name_error_component import (
            ApiV1KubernetesClustersArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesClustersArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_operator_loglevel_error_component import (
            ApiV1KubernetesClustersArchiveCreateOperatorLoglevelErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_platform_service_error_component import (
            ApiV1KubernetesClustersArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_provider_error_component import (
            ApiV1KubernetesClustersArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_provider_id_error_component import (
            ApiV1KubernetesClustersArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_provider_reference_error_component import (
            ApiV1KubernetesClustersArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_scope_error_component import (
            ApiV1KubernetesClustersArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_sla_availability_error_component import (
            ApiV1KubernetesClustersArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_sla_target_error_component import (
            ApiV1KubernetesClustersArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_slo_availability_error_component import (
            ApiV1KubernetesClustersArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_slo_target_error_component import (
            ApiV1KubernetesClustersArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_slug_error_component import (
            ApiV1KubernetesClustersArchiveCreateSlugErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_target_availability_error_component import (
            ApiV1KubernetesClustersArchiveCreateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersArchiveCreateKubeconfigCaCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersArchiveCreateKubeconfigClientCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersArchiveCreateApiServerCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateOperatorLoglevelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateAddonsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateLastBackupImportErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersArchiveCreateManagedByContentTypeErrorComponent):
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
        from ..models.api_v1_kubernetes_clusters_archive_create_active_error_component import (
            ApiV1KubernetesClustersArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_actual_availability_error_component import (
            ApiV1KubernetesClustersArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_addons_error_component import (
            ApiV1KubernetesClustersArchiveCreateAddonsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_alias_error_component import (
            ApiV1KubernetesClustersArchiveCreateAliasErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_annotations_error_component import (
            ApiV1KubernetesClustersArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersArchiveCreateApiServerCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_archived_at_error_component import (
            ApiV1KubernetesClustersArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_archived_error_component import (
            ApiV1KubernetesClustersArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_archived_reason_error_component import (
            ApiV1KubernetesClustersArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_backup_schedules_error_component import (
            ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_baserow_id_error_component import (
            ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_credential_error_component import (
            ApiV1KubernetesClustersArchiveCreateCredentialErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_criticality_error_component import (
            ApiV1KubernetesClustersArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_debug_mode_error_component import (
            ApiV1KubernetesClustersArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_description_error_component import (
            ApiV1KubernetesClustersArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesClustersArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_display_name_error_component import (
            ApiV1KubernetesClustersArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersArchiveCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_installed_error_component import (
            ApiV1KubernetesClustersArchiveCreateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_is_host_cluster_error_component import (
            ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_kind_error_component import (
            ApiV1KubernetesClustersArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersArchiveCreateKubeconfigCaCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersArchiveCreateKubeconfigClientCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_kubernetes_version_error_component import (
            ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_labels_error_component import (
            ApiV1KubernetesClustersArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_last_backup_import_error_component import (
            ApiV1KubernetesClustersArchiveCreateLastBackupImportErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_managed_by_object_id_error_component import (
            ApiV1KubernetesClustersArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_name_error_component import (
            ApiV1KubernetesClustersArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesClustersArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_operator_loglevel_error_component import (
            ApiV1KubernetesClustersArchiveCreateOperatorLoglevelErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_platform_service_error_component import (
            ApiV1KubernetesClustersArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_provider_error_component import (
            ApiV1KubernetesClustersArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_provider_id_error_component import (
            ApiV1KubernetesClustersArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_provider_reference_error_component import (
            ApiV1KubernetesClustersArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_scope_error_component import (
            ApiV1KubernetesClustersArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_sla_availability_error_component import (
            ApiV1KubernetesClustersArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_sla_target_error_component import (
            ApiV1KubernetesClustersArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_slo_availability_error_component import (
            ApiV1KubernetesClustersArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_slo_target_error_component import (
            ApiV1KubernetesClustersArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_slug_error_component import (
            ApiV1KubernetesClustersArchiveCreateSlugErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_archive_create_target_availability_error_component import (
            ApiV1KubernetesClustersArchiveCreateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClustersArchiveCreateActiveErrorComponent
                | ApiV1KubernetesClustersArchiveCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesClustersArchiveCreateAddonsErrorComponent
                | ApiV1KubernetesClustersArchiveCreateAliasErrorComponent
                | ApiV1KubernetesClustersArchiveCreateAnnotationsErrorComponent
                | ApiV1KubernetesClustersArchiveCreateApiServerCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersArchiveCreateArchivedAtErrorComponent
                | ApiV1KubernetesClustersArchiveCreateArchivedErrorComponent
                | ApiV1KubernetesClustersArchiveCreateArchivedReasonErrorComponent
                | ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponent
                | ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponent
                | ApiV1KubernetesClustersArchiveCreateCredentialErrorComponent
                | ApiV1KubernetesClustersArchiveCreateCriticalityErrorComponent
                | ApiV1KubernetesClustersArchiveCreateDebugModeErrorComponent
                | ApiV1KubernetesClustersArchiveCreateDescriptionErrorComponent
                | ApiV1KubernetesClustersArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponent
                | ApiV1KubernetesClustersArchiveCreateDisplayNameErrorComponent
                | ApiV1KubernetesClustersArchiveCreateGitlabProjectIdErrorComponent
                | ApiV1KubernetesClustersArchiveCreateInstalledErrorComponent
                | ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponent
                | ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponent
                | ApiV1KubernetesClustersArchiveCreateKindErrorComponent
                | ApiV1KubernetesClustersArchiveCreateKubeconfigCaCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersArchiveCreateKubeconfigClientCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponent
                | ApiV1KubernetesClustersArchiveCreateLabelsErrorComponent
                | ApiV1KubernetesClustersArchiveCreateLastBackupImportErrorComponent
                | ApiV1KubernetesClustersArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesClustersArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesClustersArchiveCreateNameErrorComponent
                | ApiV1KubernetesClustersArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponent
                | ApiV1KubernetesClustersArchiveCreateOperatorLoglevelErrorComponent
                | ApiV1KubernetesClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesClustersArchiveCreatePlatformServiceErrorComponent
                | ApiV1KubernetesClustersArchiveCreateProviderErrorComponent
                | ApiV1KubernetesClustersArchiveCreateProviderIdErrorComponent
                | ApiV1KubernetesClustersArchiveCreateProviderReferenceErrorComponent
                | ApiV1KubernetesClustersArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClustersArchiveCreateScopeErrorComponent
                | ApiV1KubernetesClustersArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClustersArchiveCreateSlaTargetErrorComponent
                | ApiV1KubernetesClustersArchiveCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesClustersArchiveCreateSloTargetErrorComponent
                | ApiV1KubernetesClustersArchiveCreateSlugErrorComponent
                | ApiV1KubernetesClustersArchiveCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_0 = (
                        ApiV1KubernetesClustersArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_1 = (
                        ApiV1KubernetesClustersArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_2 = (
                        ApiV1KubernetesClustersArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_3 = (
                        ApiV1KubernetesClustersArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_4 = (
                        ApiV1KubernetesClustersArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_5 = (
                        ApiV1KubernetesClustersArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_6 = (
                        ApiV1KubernetesClustersArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_7 = (
                        ApiV1KubernetesClustersArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_8 = (
                        ApiV1KubernetesClustersArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_9 = (
                        ApiV1KubernetesClustersArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_10 = (
                        ApiV1KubernetesClustersArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_11 = (
                        ApiV1KubernetesClustersArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_12 = (
                        ApiV1KubernetesClustersArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_13 = (
                        ApiV1KubernetesClustersArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_14 = (
                        ApiV1KubernetesClustersArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_15 = (
                        ApiV1KubernetesClustersArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_16 = (
                        ApiV1KubernetesClustersArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_17 = (
                        ApiV1KubernetesClustersArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_18 = (
                        ApiV1KubernetesClustersArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_19 = (
                        ApiV1KubernetesClustersArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_20 = (
                        ApiV1KubernetesClustersArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_21 = (
                        ApiV1KubernetesClustersArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_22 = (
                        ApiV1KubernetesClustersArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_23 = (
                        ApiV1KubernetesClustersArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_24 = (
                        ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_25 = (
                        ApiV1KubernetesClustersArchiveCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_26 = (
                        ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_27 = (
                        ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_28 = (
                        ApiV1KubernetesClustersArchiveCreateKubeconfigCaCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_29 = (
                        ApiV1KubernetesClustersArchiveCreateKubeconfigClientCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_30 = (
                        ApiV1KubernetesClustersArchiveCreateApiServerCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_31 = (
                        ApiV1KubernetesClustersArchiveCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_32 = (
                        ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_33 = (
                        ApiV1KubernetesClustersArchiveCreateOperatorLoglevelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_34 = (
                        ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_35 = (
                        ApiV1KubernetesClustersArchiveCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_36 = (
                        ApiV1KubernetesClustersArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_37 = (
                        ApiV1KubernetesClustersArchiveCreateAddonsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_38 = (
                        ApiV1KubernetesClustersArchiveCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_39 = (
                        ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_40 = (
                        ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_41 = (
                        ApiV1KubernetesClustersArchiveCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_42 = (
                        ApiV1KubernetesClustersArchiveCreateLastBackupImportErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_43 = (
                        ApiV1KubernetesClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_44 = (
                        ApiV1KubernetesClustersArchiveCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_45 = (
                        ApiV1KubernetesClustersArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_46 = (
                    ApiV1KubernetesClustersArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_clusters_archive_create_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_clusters_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_clusters_archive_create_validation_error.additional_properties = d
        return api_v1_kubernetes_clusters_archive_create_validation_error

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
